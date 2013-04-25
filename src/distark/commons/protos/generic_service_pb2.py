# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generic_service.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import services.simple_service_pb2
import services.dumb_service_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='generic_service.proto',
  package='master',
  serialized_pb='\n\x15generic_service.proto\x12\x06master\x1a\x1dservices/simple_service.proto\x1a\x1bservices/dumb_service.proto\"\x81\x01\n\x0cPBOneRequest\x12$\n\x05rtype\x18\x01 \x02(\x0e\x32\x15.master.PBRequestType\x12&\n\x04greq\x18\x02 \x02(\x0b\x32\x18.master.PBGenericRequest\x12#\n\tsimplereq\x18\x03 \x01(\x0b\x32\x10.PBSimpleRequest\"\xab\x01\n\rPBOneResponse\x12%\n\x05rtype\x18\x01 \x02(\x0e\x32\x16.master.PBResponseType\x12\"\n\x05\x65type\x18\x02 \x02(\x0e\x32\x13.master.PBErrorType\x12(\n\x05gresp\x18\x03 \x02(\x0b\x32\x19.master.PBGenericResponse\x12%\n\nsimpleresp\x18\x04 \x01(\x0b\x32\x11.PBSimpleResponse\"\xad\x01\n\x10PBGenericRequest\x12\x13\n\x0bservicename\x18\x01 \x02(\t\x12\x0e\n\x06\x63\x61ller\x18\x02 \x02(\t\x12\x10\n\x08ipadress\x18\x03 \x01(\t\x12\x39\n\x08priority\x18\x04 \x01(\x0e\x32\x19.master.PBRequestPriority:\x0cPRIORITY_LOW\x12\'\n\x1breq_additionaldata_donotuse\x18\x05 \x03(\tB\x02\x18\x01\"\x96\x01\n\x11PBGenericResponse\x12%\n\x03req\x18\x01 \x02(\x0b\x32\x18.master.PBGenericRequest\x12\x17\n\x0b\x63omputetime\x18\x02 \x02(\x02:\x02-1\x12\x17\n\x0fserver_ipadress\x18\x03 \x01(\t\x12(\n\x1cresp_additionaldata_donotuse\x18\x04 \x03(\tB\x02\x18\x01*#\n\rPBRequestType\x12\x12\n\x0eSIMPLE_REQUEST\x10\x01*C\n\x0ePBResponseType\x12\x1c\n\x18TECHNICAL_ERROR_RESPONSE\x10\x01\x12\x13\n\x0fSIMPLE_RESPONSE\x10\x02*\x8f\x01\n\x0bPBErrorType\x12\x0e\n\nERROR_NONE\x10\x01\x12\x19\n\x15\x45RROR_INVALID_ENVELOP\x10\x02\x12\x1b\n\x17\x45RROR_PARSING_EXCEPTION\x10\x03\x12\x19\n\x15\x45RROR_UNKNOWN_SERVICE\x10\x04\x12\x1d\n\x19\x45RROR_UNSUPPORTED_SERVICE\x10\x05*J\n\x11PBRequestPriority\x12\x11\n\rPRIORITY_HIGH\x10\x01\x12\x10\n\x0cPRIORITY_STD\x10\x02\x12\x10\n\x0cPRIORITY_LOW\x10\x03')

_PBREQUESTTYPE = _descriptor.EnumDescriptor(
  name='PBRequestType',
  full_name='master.PBRequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SIMPLE_REQUEST', index=0, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=728,
  serialized_end=763,
)

PBRequestType = enum_type_wrapper.EnumTypeWrapper(_PBREQUESTTYPE)
_PBRESPONSETYPE = _descriptor.EnumDescriptor(
  name='PBResponseType',
  full_name='master.PBResponseType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TECHNICAL_ERROR_RESPONSE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIMPLE_RESPONSE', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=765,
  serialized_end=832,
)

PBResponseType = enum_type_wrapper.EnumTypeWrapper(_PBRESPONSETYPE)
_PBERRORTYPE = _descriptor.EnumDescriptor(
  name='PBErrorType',
  full_name='master.PBErrorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ERROR_NONE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_ENVELOP', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PARSING_EXCEPTION', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNKNOWN_SERVICE', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNSUPPORTED_SERVICE', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=835,
  serialized_end=978,
)

PBErrorType = enum_type_wrapper.EnumTypeWrapper(_PBERRORTYPE)
_PBREQUESTPRIORITY = _descriptor.EnumDescriptor(
  name='PBRequestPriority',
  full_name='master.PBRequestPriority',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PRIORITY_HIGH', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRIORITY_STD', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRIORITY_LOW', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=980,
  serialized_end=1054,
)

PBRequestPriority = enum_type_wrapper.EnumTypeWrapper(_PBREQUESTPRIORITY)
SIMPLE_REQUEST = 1
TECHNICAL_ERROR_RESPONSE = 1
SIMPLE_RESPONSE = 2
ERROR_NONE = 1
ERROR_INVALID_ENVELOP = 2
ERROR_PARSING_EXCEPTION = 3
ERROR_UNKNOWN_SERVICE = 4
ERROR_UNSUPPORTED_SERVICE = 5
PRIORITY_HIGH = 1
PRIORITY_STD = 2
PRIORITY_LOW = 3



_PBONEREQUEST = _descriptor.Descriptor(
  name='PBOneRequest',
  full_name='master.PBOneRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rtype', full_name='master.PBOneRequest.rtype', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='greq', full_name='master.PBOneRequest.greq', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='simplereq', full_name='master.PBOneRequest.simplereq', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=94,
  serialized_end=223,
)


_PBONERESPONSE = _descriptor.Descriptor(
  name='PBOneResponse',
  full_name='master.PBOneResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rtype', full_name='master.PBOneResponse.rtype', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='etype', full_name='master.PBOneResponse.etype', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gresp', full_name='master.PBOneResponse.gresp', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='simpleresp', full_name='master.PBOneResponse.simpleresp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=226,
  serialized_end=397,
)


_PBGENERICREQUEST = _descriptor.Descriptor(
  name='PBGenericRequest',
  full_name='master.PBGenericRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='servicename', full_name='master.PBGenericRequest.servicename', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='caller', full_name='master.PBGenericRequest.caller', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipadress', full_name='master.PBGenericRequest.ipadress', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='priority', full_name='master.PBGenericRequest.priority', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='req_additionaldata_donotuse', full_name='master.PBGenericRequest.req_additionaldata_donotuse', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\030\001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=400,
  serialized_end=573,
)


_PBGENERICRESPONSE = _descriptor.Descriptor(
  name='PBGenericResponse',
  full_name='master.PBGenericResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='req', full_name='master.PBGenericResponse.req', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='computetime', full_name='master.PBGenericResponse.computetime', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_ipadress', full_name='master.PBGenericResponse.server_ipadress', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resp_additionaldata_donotuse', full_name='master.PBGenericResponse.resp_additionaldata_donotuse', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\030\001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=576,
  serialized_end=726,
)

_PBONEREQUEST.fields_by_name['rtype'].enum_type = _PBREQUESTTYPE
_PBONEREQUEST.fields_by_name['greq'].message_type = _PBGENERICREQUEST
_PBONEREQUEST.fields_by_name['simplereq'].message_type = services.simple_service_pb2._PBSIMPLEREQUEST
_PBONERESPONSE.fields_by_name['rtype'].enum_type = _PBRESPONSETYPE
_PBONERESPONSE.fields_by_name['etype'].enum_type = _PBERRORTYPE
_PBONERESPONSE.fields_by_name['gresp'].message_type = _PBGENERICRESPONSE
_PBONERESPONSE.fields_by_name['simpleresp'].message_type = services.simple_service_pb2._PBSIMPLERESPONSE
_PBGENERICREQUEST.fields_by_name['priority'].enum_type = _PBREQUESTPRIORITY
_PBGENERICRESPONSE.fields_by_name['req'].message_type = _PBGENERICREQUEST
DESCRIPTOR.message_types_by_name['PBOneRequest'] = _PBONEREQUEST
DESCRIPTOR.message_types_by_name['PBOneResponse'] = _PBONERESPONSE
DESCRIPTOR.message_types_by_name['PBGenericRequest'] = _PBGENERICREQUEST
DESCRIPTOR.message_types_by_name['PBGenericResponse'] = _PBGENERICRESPONSE

class PBOneRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBONEREQUEST

  # @@protoc_insertion_point(class_scope:master.PBOneRequest)

class PBOneResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBONERESPONSE

  # @@protoc_insertion_point(class_scope:master.PBOneResponse)

class PBGenericRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBGENERICREQUEST

  # @@protoc_insertion_point(class_scope:master.PBGenericRequest)

class PBGenericResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBGENERICRESPONSE

  # @@protoc_insertion_point(class_scope:master.PBGenericResponse)


_PBGENERICREQUEST.fields_by_name['req_additionaldata_donotuse'].has_options = True
_PBGENERICREQUEST.fields_by_name['req_additionaldata_donotuse']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\030\001')
_PBGENERICRESPONSE.fields_by_name['resp_additionaldata_donotuse'].has_options = True
_PBGENERICRESPONSE.fields_by_name['resp_additionaldata_donotuse']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\030\001')
# @@protoc_insertion_point(module_scope)
