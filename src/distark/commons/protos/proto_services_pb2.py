# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto_services.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto_services.proto',
  package='master',
  serialized_pb='\n\x14proto_services.proto\x12\x06master\"\xa9\x01\n\x0eGenericRequest\x12\x13\n\x0bservicename\x18\x01 \x02(\t\x12\x0e\n\x06\x63\x61ller\x18\x02 \x02(\t\x12\x10\n\x08ipadress\x18\x03 \x01(\t\x12\x37\n\x08priority\x18\x04 \x01(\x0e\x32\x17.master.RequestPriority:\x0cPRIORITY_LOW\x12\'\n\x1breq_additionaldata_donotuse\x18\x05 \x03(\tB\x02\x18\x01\"\x92\x01\n\x0fGenericResponse\x12#\n\x03req\x18\x01 \x02(\x0b\x32\x16.master.GenericRequest\x12\x17\n\x0b\x63omputetime\x18\x02 \x02(\x02:\x02-1\x12\x17\n\x0fserver_ipadress\x18\x03 \x01(\t\x12(\n\x1cresp_additionaldata_donotuse\x18\x04 \x03(\tB\x02\x18\x01\"\x1f\n\rSimpleRequest\x12\x0e\n\x06youpla\x18\x01 \x02(\t\"\x1e\n\x0eSimpleResponse\x12\x0c\n\x04\x62oum\x18\x01 \x02(\t\"\x9f\x01\n\nOneRequest\x12!\n\x04type\x18\x01 \x02(\x0e\x32\x13.master.RequestType\x12$\n\x04greq\x18\x02 \x02(\x0b\x32\x16.master.GenericRequest\x12(\n\tsimplereq\x18\x03 \x01(\x0b\x32\x15.master.SimpleRequest\x12\x1e\n\x06\x66ooreq\x18\x04 \x01(\x0b\x32\x0e.master.FooReq\"\x19\n\x06\x46ooReq\x12\x0f\n\x07\x62oisson\x18\x01 \x02(\t\"\x1a\n\x07\x42\x61rResp\x12\x0f\n\x07\x62oisson\x18\x01 \x02(\t\"\xa7\x01\n\x0bOneResponse\x12\"\n\x04type\x18\x01 \x02(\x0e\x32\x14.master.ResponseType\x12&\n\x05gresp\x18\x02 \x02(\x0b\x32\x17.master.GenericResponse\x12*\n\nsimpleresp\x18\x03 \x01(\x0b\x32\x16.master.SimpleResponse\x12 \n\x07\x62\x61rresp\x18\x04 \x01(\x0b\x32\x0f.master.BarResp*H\n\x0fRequestPriority\x12\x11\n\rPRIORITY_HIGH\x10\x01\x12\x10\n\x0cPRIORITY_STD\x10\x02\x12\x10\n\x0cPRIORITY_LOW\x10\x03**\n\x0bRequestType\x12\x12\n\x0eSIMPLE_REQUEST\x10\x01\x12\x07\n\x03\x46OO\x10\x02*Z\n\x0cResponseType\x12\x13\n\x0fUNKNOWN_SERVICE\x10\x01\x12\x17\n\x13UNSUPPORTED_SERVICE\x10\x02\x12\x13\n\x0fSIMPLE_RESPONSE\x10\x03\x12\x07\n\x03\x42\x41R\x10\x04')

_REQUESTPRIORITY = _descriptor.EnumDescriptor(
  name='RequestPriority',
  full_name='master.RequestPriority',
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
  serialized_start=805,
  serialized_end=877,
)

RequestPriority = enum_type_wrapper.EnumTypeWrapper(_REQUESTPRIORITY)
_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='master.RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SIMPLE_REQUEST', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOO', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=879,
  serialized_end=921,
)

RequestType = enum_type_wrapper.EnumTypeWrapper(_REQUESTTYPE)
_RESPONSETYPE = _descriptor.EnumDescriptor(
  name='ResponseType',
  full_name='master.ResponseType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_SERVICE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_SERVICE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIMPLE_RESPONSE', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAR', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=923,
  serialized_end=1013,
)

ResponseType = enum_type_wrapper.EnumTypeWrapper(_RESPONSETYPE)
PRIORITY_HIGH = 1
PRIORITY_STD = 2
PRIORITY_LOW = 3
SIMPLE_REQUEST = 1
FOO = 2
UNKNOWN_SERVICE = 1
UNSUPPORTED_SERVICE = 2
SIMPLE_RESPONSE = 3
BAR = 4



_GENERICREQUEST = _descriptor.Descriptor(
  name='GenericRequest',
  full_name='master.GenericRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='servicename', full_name='master.GenericRequest.servicename', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='caller', full_name='master.GenericRequest.caller', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipadress', full_name='master.GenericRequest.ipadress', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='priority', full_name='master.GenericRequest.priority', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='req_additionaldata_donotuse', full_name='master.GenericRequest.req_additionaldata_donotuse', index=4,
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
  serialized_start=33,
  serialized_end=202,
)


_GENERICRESPONSE = _descriptor.Descriptor(
  name='GenericResponse',
  full_name='master.GenericResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='req', full_name='master.GenericResponse.req', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='computetime', full_name='master.GenericResponse.computetime', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_ipadress', full_name='master.GenericResponse.server_ipadress', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resp_additionaldata_donotuse', full_name='master.GenericResponse.resp_additionaldata_donotuse', index=3,
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
  serialized_start=205,
  serialized_end=351,
)


_SIMPLEREQUEST = _descriptor.Descriptor(
  name='SimpleRequest',
  full_name='master.SimpleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='youpla', full_name='master.SimpleRequest.youpla', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=353,
  serialized_end=384,
)


_SIMPLERESPONSE = _descriptor.Descriptor(
  name='SimpleResponse',
  full_name='master.SimpleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boum', full_name='master.SimpleResponse.boum', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=386,
  serialized_end=416,
)


_ONEREQUEST = _descriptor.Descriptor(
  name='OneRequest',
  full_name='master.OneRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='master.OneRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='greq', full_name='master.OneRequest.greq', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='simplereq', full_name='master.OneRequest.simplereq', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fooreq', full_name='master.OneRequest.fooreq', index=3,
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
  serialized_start=419,
  serialized_end=578,
)


_FOOREQ = _descriptor.Descriptor(
  name='FooReq',
  full_name='master.FooReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boisson', full_name='master.FooReq.boisson', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=580,
  serialized_end=605,
)


_BARRESP = _descriptor.Descriptor(
  name='BarResp',
  full_name='master.BarResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boisson', full_name='master.BarResp.boisson', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=607,
  serialized_end=633,
)


_ONERESPONSE = _descriptor.Descriptor(
  name='OneResponse',
  full_name='master.OneResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='master.OneResponse.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gresp', full_name='master.OneResponse.gresp', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='simpleresp', full_name='master.OneResponse.simpleresp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='barresp', full_name='master.OneResponse.barresp', index=3,
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
  serialized_start=636,
  serialized_end=803,
)

_GENERICREQUEST.fields_by_name['priority'].enum_type = _REQUESTPRIORITY
_GENERICRESPONSE.fields_by_name['req'].message_type = _GENERICREQUEST
_ONEREQUEST.fields_by_name['type'].enum_type = _REQUESTTYPE
_ONEREQUEST.fields_by_name['greq'].message_type = _GENERICREQUEST
_ONEREQUEST.fields_by_name['simplereq'].message_type = _SIMPLEREQUEST
_ONEREQUEST.fields_by_name['fooreq'].message_type = _FOOREQ
_ONERESPONSE.fields_by_name['type'].enum_type = _RESPONSETYPE
_ONERESPONSE.fields_by_name['gresp'].message_type = _GENERICRESPONSE
_ONERESPONSE.fields_by_name['simpleresp'].message_type = _SIMPLERESPONSE
_ONERESPONSE.fields_by_name['barresp'].message_type = _BARRESP
DESCRIPTOR.message_types_by_name['GenericRequest'] = _GENERICREQUEST
DESCRIPTOR.message_types_by_name['GenericResponse'] = _GENERICRESPONSE
DESCRIPTOR.message_types_by_name['SimpleRequest'] = _SIMPLEREQUEST
DESCRIPTOR.message_types_by_name['SimpleResponse'] = _SIMPLERESPONSE
DESCRIPTOR.message_types_by_name['OneRequest'] = _ONEREQUEST
DESCRIPTOR.message_types_by_name['FooReq'] = _FOOREQ
DESCRIPTOR.message_types_by_name['BarResp'] = _BARRESP
DESCRIPTOR.message_types_by_name['OneResponse'] = _ONERESPONSE

class GenericRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GENERICREQUEST

  # @@protoc_insertion_point(class_scope:master.GenericRequest)

class GenericResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GENERICRESPONSE

  # @@protoc_insertion_point(class_scope:master.GenericResponse)

class SimpleRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SIMPLEREQUEST

  # @@protoc_insertion_point(class_scope:master.SimpleRequest)

class SimpleResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SIMPLERESPONSE

  # @@protoc_insertion_point(class_scope:master.SimpleResponse)

class OneRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ONEREQUEST

  # @@protoc_insertion_point(class_scope:master.OneRequest)

class FooReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FOOREQ

  # @@protoc_insertion_point(class_scope:master.FooReq)

class BarResp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BARRESP

  # @@protoc_insertion_point(class_scope:master.BarResp)

class OneResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ONERESPONSE

  # @@protoc_insertion_point(class_scope:master.OneResponse)


_GENERICREQUEST.fields_by_name['req_additionaldata_donotuse'].has_options = True
_GENERICREQUEST.fields_by_name['req_additionaldata_donotuse']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\030\001')
_GENERICRESPONSE.fields_by_name['resp_additionaldata_donotuse'].has_options = True
_GENERICRESPONSE.fields_by_name['resp_additionaldata_donotuse']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\030\001')
# @@protoc_insertion_point(module_scope)
