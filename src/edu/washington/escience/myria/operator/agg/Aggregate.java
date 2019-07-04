package edu.washington.escience.myria.operator.agg;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;

import javax.annotation.Nullable;

import com.google.common.base.Preconditions;
import com.google.common.collect.ImmutableMap;

import edu.washington.escience.myria.DbException;
import edu.washington.escience.myria.Schema;
import edu.washington.escience.myria.column.Column;
import edu.washington.escience.myria.expression.Expression;
import edu.washington.escience.myria.expression.evaluate.ExpressionOperatorParameter;
import edu.washington.escience.myria.expression.evaluate.GenericEvaluator;
import edu.washington.escience.myria.expression.evaluate.PythonUDFEvaluator;
import edu.washington.escience.myria.functions.PythonFunctionRegistrar;
import edu.washington.escience.myria.operator.Operator;
import edu.washington.escience.myria.operator.UnaryOperator;
import edu.washington.escience.myria.operator.UniqueTupleHashTable;
import edu.washington.escience.myria.operator.agg.PrimitiveAggregator.AggregationOp;
import edu.washington.escience.myria.storage.TupleBatch;
import edu.washington.escience.myria.storage.TupleBatchBuffer;
import edu.washington.escience.myria.util.MyriaArrayUtils;

/**
 * The Aggregation operator that computes an aggregate (e.g., sum, avg, max, min). This variant supports aggregates over
 * multiple columns, group by multiple columns.
 */
public class Aggregate extends UnaryOperator {

  /** Java requires this. **/
  private static final long serialVersionUID = 1L;

  /** The hash table containing groups and states. */
  protected transient UniqueTupleHashTable groupStates;
  /** Factories to make the Aggregators. **/
  private final AggregatorFactory[] factories;
  /** Aggregators of the internal state. */
  protected List<Aggregator> internalAggs;
  /** Expressions that emit output. */
  protected List<GenericEvaluator> emitEvals;
  /** Group fields. Empty array means no grouping. **/
  protected final int[] gfields;
  /** Buffer for restoring results. */
  protected TupleBatchBuffer resultBuffer;

  /**
   * Groups the input tuples according to the specified grouping fields, then produces the specified aggregates.
   *
   * @param child The Operator that is feeding us tuples.
   * @param gfields The columns over which we are grouping the result. Null means no group by.
   * @param factories The factories that will produce the {@link Aggregator}s;
   */
  public Aggregate(
      @Nullable final Operator child, final int[] gfields, final AggregatorFactory... factories) {
    super(child);
    this.gfields = gfields;
    this.factories = Objects.requireNonNull(factories, "factories");
  }

  @Override
  protected void cleanup() throws DbException {
    groupStates.cleanup();
    resultBuffer.clear();
  }

  /**
   * Returns the next tuple. The first few columns are group-by fields if there are any, followed by columns of
   * aggregate results generated by {@link Aggregate#emitEvals}.
   *
   * @throws DbException if any error occurs.
   * @return result TB.
   */
  @Override
  protected TupleBatch fetchNextReady() throws DbException {
    final Operator child = getChild();
    TupleBatch tb = child.nextReady();
    while (tb != null) {
      for (int row = 0; row < tb.numTuples(); ++row) {
        int index = groupStates.getIndex(tb, gfields, row);
        if (index == -1) {
          groupStates.addTuple(tb, gfields, row, true);
          int offset = gfields.length;
          for (Aggregator agg : internalAggs) {
            agg.initState(groupStates.getData(), offset);
            offset += agg.getStateSize();
          }
          index = groupStates.numTuples() - 1;
        }
        int offset = gfields.length;
        for (Aggregator agg : internalAggs) {
          agg.addRow(tb, row, groupStates.getData(), index, offset);
          offset += agg.getStateSize();
        }
      }
      tb = child.nextReady();
    }
    if (child.eos()) {
      /* Special check for count(*) as the only aggregate on an empty relation: emit 0. */
      if (getNumOutputTuples() == 0 && groupStates.numTuples() == 0 && isCountAllOnlyAggregate()) {
        resultBuffer.putLong(0, 0);
      }
      generateResult();
      return resultBuffer.popAny();
    }
    return null;
  }

  /**
   * Check if count(*) is the only aggregate with no group by.
   * */
  private boolean isCountAllOnlyAggregate() {
    return gfields.length == 0
        && internalAggs.size() == 1
        && internalAggs.get(0) instanceof PrimitiveAggregator
        && ((PrimitiveAggregator) (internalAggs.get(0))).aggOp == AggregationOp.COUNT;
  }

  /**
   * @return A batch's worth of result tuples from this aggregate.
   * @throws DbException if there is an error.
   */
  protected void generateResult() throws DbException {
    if (groupStates.numTuples() == 0) {
      return;
    }
    int stateOffset = gfields.length;
    for (Aggregator agg : internalAggs) {
      if (agg instanceof UserDefinedAggregator) {
        ((UserDefinedAggregator) agg).finalizePythonUpdaters(groupStates.getData(), stateOffset);
      }
      stateOffset += agg.getStateSize();
    }
    Schema inputSchema = getChild().getSchema();
    for (TupleBatch tb : groupStates.getData().getAll()) {
      List<Column<?>> columns = new ArrayList<Column<?>>();
      columns.addAll(tb.getDataColumns().subList(0, gfields.length));
      stateOffset = gfields.length;
      int emitOffset = 0;
      for (AggregatorFactory factory : factories) {
        int stateSize = factory.generateStateSchema(inputSchema).numColumns();
        int emitSize = factory.generateSchema(inputSchema).numColumns();
        TupleBatch state = tb.selectColumns(MyriaArrayUtils.range(stateOffset, stateSize));
        for (GenericEvaluator eval : emitEvals.subList(emitOffset, emitOffset + emitSize)) {
          columns.add(eval.evalTupleBatch(state, getSchema()).getResultColumns().get(0));
        }
        stateOffset += stateSize;
        emitOffset += emitSize;
      }
      addToResult(columns);
    }
    groupStates.cleanup();
  }

  /**
   * @param columns result columns.
   */
  protected void addToResult(List<Column<?>> columns) {
    resultBuffer.absorb(new TupleBatch(getSchema(), columns), true);
  }
  /**
   * The schema of the aggregate output. Grouping fields first and then aggregate fields. The aggregate
   *
   * @return the resulting schema
   */
  @Override
  protected Schema generateSchema() {
    if (getChild() == null || getChild().getSchema() == null) {
      return null;
    }
    Schema inputSchema = getChild().getSchema();
    if (inputSchema == null) {
      return null;
    }
    Schema aggSchema = Schema.EMPTY_SCHEMA;
    for (int i = 0; i < factories.length; ++i) {
      aggSchema = Schema.merge(aggSchema, factories[i].generateSchema(inputSchema));
    }
    return Schema.merge(inputSchema.getSubSchema(gfields), aggSchema);
  }

  @Override
  protected void init(final ImmutableMap<String, Object> execEnvVars) throws DbException {
    Schema inputSchema = getChild().getSchema();
    Preconditions.checkState(inputSchema != null, "unable to determine schema in init");
    internalAggs = new ArrayList<Aggregator>();
    emitEvals = new ArrayList<GenericEvaluator>();
    Schema groupingSchema = inputSchema.getSubSchema(gfields);
    Schema stateSchema = Schema.EMPTY_SCHEMA;
    PythonFunctionRegistrar pyFuncReg = getPythonFunctionRegistrar();
    for (AggregatorFactory factory : factories) {
      factory.setPyFuncReg(pyFuncReg);
      internalAggs.addAll(factory.generateInternalAggs(inputSchema));
      List<Expression> emits = factory.generateEmitExpressions(inputSchema);
      Schema newStateSchema = factory.generateStateSchema(inputSchema);
      stateSchema = Schema.merge(stateSchema, newStateSchema);
      for (Expression exp : emits) {
        GenericEvaluator evaluator = null;
        if (exp.isRegisteredPythonUDF()) {
          evaluator =
              new PythonUDFEvaluator(
                  exp,
                  new ExpressionOperatorParameter(
                      inputSchema, stateSchema, getPythonFunctionRegistrar()));
        } else {
          evaluator =
              new GenericEvaluator(
                  exp,
                  new ExpressionOperatorParameter(
                      newStateSchema, newStateSchema, getPythonFunctionRegistrar()));
        }
        emitEvals.add(evaluator);
      }
    }
    groupStates =
        new UniqueTupleHashTable(
            Schema.merge(groupingSchema, stateSchema), MyriaArrayUtils.range(0, gfields.length));
    resultBuffer = new TupleBatchBuffer(getSchema());
    groupStates.name = "op" + getOpId();
  }

  @Override
  public Map<String, Map<String, Integer>> dumpHashTableStats() {
    Map<String, Map<String, Integer>> ret = new HashMap<>();
    if (groupStates != null) {
      ret.put(groupStates.name, groupStates.dumpStats());
    }
    return ret;
  }
};