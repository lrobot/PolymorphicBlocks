"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12edgir/common.proto\x12\x0cedgir.common"\x95\x03\n\x08Metadata\x12&\n\x07unknown\x18\x01 \x01(\x0b2\x13.edgir.common.EmptyH\x00\x12\x0f\n\x05known\x18\x02 \x01(\tH\x00\x121\n\x07members\x18e \x01(\x0b2\x1e.edgir.common.Metadata.MembersH\x01\x12\x13\n\ttext_leaf\x18f \x01(\tH\x01\x12\x12\n\x08bin_leaf\x18g \x01(\x0cH\x01\x125\n\x0esource_locator\x18n \x01(\x0b2\x1b.edgir.common.SourceLocatorH\x01\x12$\n\x05error\x18p \x01(\x0b2\x13.edgir.common.ErrorH\x01\x1a\x86\x01\n\x07Members\x126\n\x04node\x18\n \x03(\x0b2(.edgir.common.Metadata.Members.NodeEntry\x1aC\n\tNodeEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.edgir.common.Metadata:\x028\x01B\x06\n\x04typeB\x06\n\x04meta"\xc9\x01\n\rSourceLocator\x12\x14\n\x0cfile_package\x18\x01 \x01(\t\x12\x13\n\x0bline_offset\x18\x02 \x01(\x05\x12\x12\n\ncol_offset\x18\x03 \x01(\x05\x12;\n\x0bsource_type\x18\x04 \x01(\x0e2&.edgir.common.SourceLocator.SourceType"<\n\nSourceType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nDEFINITION\x10\x01\x12\x11\n\rINSTANTIATION\x10\x02"X\n\x05Error\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x11\n\ttraceback\x18\x03 \x01(\t\x12+\n\x06source\x18\x02 \x03(\x0b2\x1b.edgir.common.SourceLocator"\x07\n\x05Emptyb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgir.common_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _METADATA_MEMBERS_NODEENTRY._options = None
    _METADATA_MEMBERS_NODEENTRY._serialized_options = b'8\x01'
    _METADATA._serialized_start = 37
    _METADATA._serialized_end = 442
    _METADATA_MEMBERS._serialized_start = 292
    _METADATA_MEMBERS._serialized_end = 426
    _METADATA_MEMBERS_NODEENTRY._serialized_start = 359
    _METADATA_MEMBERS_NODEENTRY._serialized_end = 426
    _SOURCELOCATOR._serialized_start = 445
    _SOURCELOCATOR._serialized_end = 646
    _SOURCELOCATOR_SOURCETYPE._serialized_start = 586
    _SOURCELOCATOR_SOURCETYPE._serialized_end = 646
    _ERROR._serialized_start = 648
    _ERROR._serialized_end = 736
    _EMPTY._serialized_start = 738
    _EMPTY._serialized_end = 745