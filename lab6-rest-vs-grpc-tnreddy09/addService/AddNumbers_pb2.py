# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AddNumbers.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='AddNumbers.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10\x41\x64\x64Numbers.proto\"\x1d\n\x05input\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\t\n\x01\x62\x18\x02 \x01(\x05\"\x17\n\x06Number\x12\r\n\x05value\x18\x03 \x01(\x05\x32-\n\nAddNumbers\x12\x1f\n\nAddNumbers\x12\x06.input\x1a\x07.Number\"\x00\x62\x06proto3')
)




_INPUT = _descriptor.Descriptor(
  name='input',
  full_name='input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='input.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='input.b', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=49,
)


_NUMBER = _descriptor.Descriptor(
  name='Number',
  full_name='Number',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Number.value', index=0,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=74,
)

DESCRIPTOR.message_types_by_name['input'] = _INPUT
DESCRIPTOR.message_types_by_name['Number'] = _NUMBER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

input = _reflection.GeneratedProtocolMessageType('input', (_message.Message,), {
  'DESCRIPTOR' : _INPUT,
  '__module__' : 'AddNumbers_pb2'
  # @@protoc_insertion_point(class_scope:input)
  })
_sym_db.RegisterMessage(input)

Number = _reflection.GeneratedProtocolMessageType('Number', (_message.Message,), {
  'DESCRIPTOR' : _NUMBER,
  '__module__' : 'AddNumbers_pb2'
  # @@protoc_insertion_point(class_scope:Number)
  })
_sym_db.RegisterMessage(Number)



_ADDNUMBERS = _descriptor.ServiceDescriptor(
  name='AddNumbers',
  full_name='AddNumbers',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=76,
  serialized_end=121,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddNumbers',
    full_name='AddNumbers.AddNumbers',
    index=0,
    containing_service=None,
    input_type=_INPUT,
    output_type=_NUMBER,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ADDNUMBERS)

DESCRIPTOR.services_by_name['AddNumbers'] = _ADDNUMBERS

# @@protoc_insertion_point(module_scope)
