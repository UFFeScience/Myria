# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: control.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='control.proto',
  package='',
  serialized_pb='\n\rcontrol.proto\"\xe3\x02\n\x0e\x43ontrolMessage\x12\"\n\x04type\x18\x01 \x02(\x0e\x32\x14.ControlMessage.Type\x12\x11\n\tworker_id\x18\x02 \x01(\x05\x12#\n\x0eremote_address\x18\x03 \x01(\x0b\x32\x0b.SocketInfo\x12&\n\x0eresource_stats\x18\x04 \x03(\x0b\x32\x0e.ResourceStats\x12\x18\n\x10\x61\x63ked_worker_ids\x18\x05 \x03(\x05\x12$\n\x10worker_exception\x18\x06 \x01(\x0b\x32\n.Exception\"\x8c\x01\n\x04Type\x12\x0c\n\x08SHUTDOWN\x10\x01\x12\x14\n\x10WORKER_HEARTBEAT\x10\x02\x12\x11\n\rREMOVE_WORKER\x10\x03\x12\x0e\n\nADD_WORKER\x10\x04\x12\x15\n\x11REMOVE_WORKER_ACK\x10\x05\x12\x12\n\x0e\x41\x44\x44_WORKER_ACK\x10\x06\x12\x12\n\x0eRESOURCE_STATS\x10\x07\"\x1e\n\tException\x12\x11\n\texception\x18\x01 \x02(\x0c\"(\n\nSocketInfo\x12\x0c\n\x04host\x18\x01 \x02(\t\x12\x0c\n\x04port\x18\x02 \x02(\x05\"y\n\rResourceStats\x12\x11\n\ttimestamp\x18\x01 \x02(\x03\x12\x0c\n\x04opId\x18\x02 \x02(\x05\x12\x13\n\x0bmeasurement\x18\x03 \x02(\t\x12\r\n\x05value\x18\x04 \x02(\x03\x12\x0f\n\x07queryId\x18\x05 \x02(\x03\x12\x12\n\nsubqueryId\x18\x06 \x02(\x03\x42\x33\n#edu.washington.escience.myria.protoB\x0c\x43ontrolProto')



_CONTROLMESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='ControlMessage.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SHUTDOWN', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORKER_HEARTBEAT', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE_WORKER', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADD_WORKER', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE_WORKER_ACK', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADD_WORKER_ACK', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESOURCE_STATS', index=6, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=233,
  serialized_end=373,
)


_CONTROLMESSAGE = _descriptor.Descriptor(
  name='ControlMessage',
  full_name='ControlMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ControlMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='worker_id', full_name='ControlMessage.worker_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remote_address', full_name='ControlMessage.remote_address', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource_stats', full_name='ControlMessage.resource_stats', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acked_worker_ids', full_name='ControlMessage.acked_worker_ids', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='worker_exception', full_name='ControlMessage.worker_exception', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONTROLMESSAGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=18,
  serialized_end=373,
)


_EXCEPTION = _descriptor.Descriptor(
  name='Exception',
  full_name='Exception',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exception', full_name='Exception.exception', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=375,
  serialized_end=405,
)


_SOCKETINFO = _descriptor.Descriptor(
  name='SocketInfo',
  full_name='SocketInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='SocketInfo.host', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='SocketInfo.port', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=407,
  serialized_end=447,
)


_RESOURCESTATS = _descriptor.Descriptor(
  name='ResourceStats',
  full_name='ResourceStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ResourceStats.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='opId', full_name='ResourceStats.opId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='measurement', full_name='ResourceStats.measurement', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='ResourceStats.value', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='queryId', full_name='ResourceStats.queryId', index=4,
      number=5, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subqueryId', full_name='ResourceStats.subqueryId', index=5,
      number=6, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=449,
  serialized_end=570,
)

_CONTROLMESSAGE.fields_by_name['type'].enum_type = _CONTROLMESSAGE_TYPE
_CONTROLMESSAGE.fields_by_name['remote_address'].message_type = _SOCKETINFO
_CONTROLMESSAGE.fields_by_name['resource_stats'].message_type = _RESOURCESTATS
_CONTROLMESSAGE.fields_by_name['worker_exception'].message_type = _EXCEPTION
_CONTROLMESSAGE_TYPE.containing_type = _CONTROLMESSAGE;
DESCRIPTOR.message_types_by_name['ControlMessage'] = _CONTROLMESSAGE
DESCRIPTOR.message_types_by_name['Exception'] = _EXCEPTION
DESCRIPTOR.message_types_by_name['SocketInfo'] = _SOCKETINFO
DESCRIPTOR.message_types_by_name['ResourceStats'] = _RESOURCESTATS

class ControlMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONTROLMESSAGE

  # @@protoc_insertion_point(class_scope:ControlMessage)

class Exception(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXCEPTION

  # @@protoc_insertion_point(class_scope:Exception)

class SocketInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SOCKETINFO

  # @@protoc_insertion_point(class_scope:SocketInfo)

class ResourceStats(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESOURCESTATS

  # @@protoc_insertion_point(class_scope:ResourceStats)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n#edu.washington.escience.myria.protoB\014ControlProto')
# @@protoc_insertion_point(module_scope)
