# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from .common_pb2 import (
    Empty as common_pb2___Empty,
    Metadata as common_pb2___Metadata,
)

from .expr_pb2 import (
    ValueExpr as expr_pb2___ValueExpr,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from .init_pb2 import (
    ValInit as init_pb2___ValInit,
)

from .ref_pb2 import (
    LibraryPath as ref_pb2___LibraryPath,
)

from typing import (
    Iterable as typing___Iterable,
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class Port(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ParamsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> init_pb2___ValInit: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[init_pb2___ValInit] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Port.ParamsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Port.ParamsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class ConstraintsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> expr_pb2___ValueExpr: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[expr_pb2___ValueExpr] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Port.ConstraintsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Port.ConstraintsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...


    @property
    def params(self) -> typing___MutableMapping[typing___Text, init_pb2___ValInit]: ...

    @property
    def constraints(self) -> typing___MutableMapping[typing___Text, expr_pb2___ValueExpr]: ...

    @property
    def superclasses(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ref_pb2___LibraryPath]: ...

    @property
    def meta(self) -> common_pb2___Metadata: ...

    def __init__(self,
        *,
        params : typing___Optional[typing___Mapping[typing___Text, init_pb2___ValInit]] = None,
        constraints : typing___Optional[typing___Mapping[typing___Text, expr_pb2___ValueExpr]] = None,
        superclasses : typing___Optional[typing___Iterable[ref_pb2___LibraryPath]] = None,
        meta : typing___Optional[common_pb2___Metadata] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Port: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Port: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"meta",b"meta"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"constraints",b"constraints",u"meta",b"meta",u"params",b"params",u"superclasses",b"superclasses"]) -> None: ...

class Bundle(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ParamsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> init_pb2___ValInit: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[init_pb2___ValInit] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Bundle.ParamsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Bundle.ParamsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class PortsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> PortLike: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[PortLike] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Bundle.PortsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Bundle.PortsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class ConstraintsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> expr_pb2___ValueExpr: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[expr_pb2___ValueExpr] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Bundle.ConstraintsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Bundle.ConstraintsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...


    @property
    def params(self) -> typing___MutableMapping[typing___Text, init_pb2___ValInit]: ...

    @property
    def ports(self) -> typing___MutableMapping[typing___Text, PortLike]: ...

    @property
    def constraints(self) -> typing___MutableMapping[typing___Text, expr_pb2___ValueExpr]: ...

    @property
    def superclasses(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ref_pb2___LibraryPath]: ...

    @property
    def meta(self) -> common_pb2___Metadata: ...

    def __init__(self,
        *,
        params : typing___Optional[typing___Mapping[typing___Text, init_pb2___ValInit]] = None,
        ports : typing___Optional[typing___Mapping[typing___Text, PortLike]] = None,
        constraints : typing___Optional[typing___Mapping[typing___Text, expr_pb2___ValueExpr]] = None,
        superclasses : typing___Optional[typing___Iterable[ref_pb2___LibraryPath]] = None,
        meta : typing___Optional[common_pb2___Metadata] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Bundle: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Bundle: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"meta",b"meta"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"constraints",b"constraints",u"meta",b"meta",u"params",b"params",u"ports",b"ports",u"superclasses",b"superclasses"]) -> None: ...

class PortArray(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class PortsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> PortLike: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[PortLike] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> PortArray.PortsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PortArray.PortsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...


    @property
    def superclasses(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ref_pb2___LibraryPath]: ...

    @property
    def ports(self) -> typing___MutableMapping[typing___Text, PortLike]: ...

    @property
    def meta(self) -> common_pb2___Metadata: ...

    def __init__(self,
        *,
        superclasses : typing___Optional[typing___Iterable[ref_pb2___LibraryPath]] = None,
        ports : typing___Optional[typing___Mapping[typing___Text, PortLike]] = None,
        meta : typing___Optional[common_pb2___Metadata] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PortArray: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PortArray: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"meta",b"meta"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"meta",b"meta",u"ports",b"ports",u"superclasses",b"superclasses"]) -> None: ...

class PortLike(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def undefined(self) -> common_pb2___Empty: ...

    @property
    def lib_elem(self) -> ref_pb2___LibraryPath: ...

    @property
    def port(self) -> Port: ...

    @property
    def array(self) -> PortArray: ...

    @property
    def bundle(self) -> Bundle: ...

    def __init__(self,
        *,
        undefined : typing___Optional[common_pb2___Empty] = None,
        lib_elem : typing___Optional[ref_pb2___LibraryPath] = None,
        port : typing___Optional[Port] = None,
        array : typing___Optional[PortArray] = None,
        bundle : typing___Optional[Bundle] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PortLike: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PortLike: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"array",b"array",u"bundle",b"bundle",u"is",b"is",u"lib_elem",b"lib_elem",u"port",b"port",u"undefined",b"undefined"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"array",b"array",u"bundle",b"bundle",u"is",b"is",u"lib_elem",b"lib_elem",u"port",b"port",u"undefined",b"undefined"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"is",b"is"]) -> typing_extensions___Literal["undefined","lib_elem","port","array","bundle"]: ...

class HierarchyBlock(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ParamsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> init_pb2___ValInit: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[init_pb2___ValInit] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> HierarchyBlock.ParamsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> HierarchyBlock.ParamsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class PortsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> PortLike: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[PortLike] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> HierarchyBlock.PortsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> HierarchyBlock.PortsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class BlocksEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> BlockLike: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[BlockLike] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> HierarchyBlock.BlocksEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> HierarchyBlock.BlocksEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class LinksEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> LinkLike: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[LinkLike] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> HierarchyBlock.LinksEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> HierarchyBlock.LinksEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class ConstraintsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> expr_pb2___ValueExpr: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[expr_pb2___ValueExpr] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> HierarchyBlock.ConstraintsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> HierarchyBlock.ConstraintsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...


    @property
    def params(self) -> typing___MutableMapping[typing___Text, init_pb2___ValInit]: ...

    @property
    def ports(self) -> typing___MutableMapping[typing___Text, PortLike]: ...

    @property
    def blocks(self) -> typing___MutableMapping[typing___Text, BlockLike]: ...

    @property
    def links(self) -> typing___MutableMapping[typing___Text, LinkLike]: ...

    @property
    def constraints(self) -> typing___MutableMapping[typing___Text, expr_pb2___ValueExpr]: ...

    @property
    def superclasses(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ref_pb2___LibraryPath]: ...

    @property
    def meta(self) -> common_pb2___Metadata: ...

    def __init__(self,
        *,
        params : typing___Optional[typing___Mapping[typing___Text, init_pb2___ValInit]] = None,
        ports : typing___Optional[typing___Mapping[typing___Text, PortLike]] = None,
        blocks : typing___Optional[typing___Mapping[typing___Text, BlockLike]] = None,
        links : typing___Optional[typing___Mapping[typing___Text, LinkLike]] = None,
        constraints : typing___Optional[typing___Mapping[typing___Text, expr_pb2___ValueExpr]] = None,
        superclasses : typing___Optional[typing___Iterable[ref_pb2___LibraryPath]] = None,
        meta : typing___Optional[common_pb2___Metadata] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> HierarchyBlock: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> HierarchyBlock: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"meta",b"meta"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"blocks",b"blocks",u"constraints",b"constraints",u"links",b"links",u"meta",b"meta",u"params",b"params",u"ports",b"ports",u"superclasses",b"superclasses"]) -> None: ...

class BlockLike(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def undefined(self) -> common_pb2___Empty: ...

    @property
    def lib_elem(self) -> ref_pb2___LibraryPath: ...

    @property
    def hierarchy(self) -> HierarchyBlock: ...

    def __init__(self,
        *,
        undefined : typing___Optional[common_pb2___Empty] = None,
        lib_elem : typing___Optional[ref_pb2___LibraryPath] = None,
        hierarchy : typing___Optional[HierarchyBlock] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> BlockLike: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> BlockLike: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"hierarchy",b"hierarchy",u"lib_elem",b"lib_elem",u"type",b"type",u"undefined",b"undefined"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"hierarchy",b"hierarchy",u"lib_elem",b"lib_elem",u"type",b"type",u"undefined",b"undefined"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"type",b"type"]) -> typing_extensions___Literal["undefined","lib_elem","hierarchy"]: ...

class Link(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ParamsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> init_pb2___ValInit: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[init_pb2___ValInit] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Link.ParamsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Link.ParamsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class PortsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> PortLike: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[PortLike] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Link.PortsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Link.PortsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class LinksEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> LinkLike: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[LinkLike] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Link.LinksEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Link.LinksEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class ConstraintsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> expr_pb2___ValueExpr: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[expr_pb2___ValueExpr] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Link.ConstraintsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Link.ConstraintsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...


    @property
    def params(self) -> typing___MutableMapping[typing___Text, init_pb2___ValInit]: ...

    @property
    def ports(self) -> typing___MutableMapping[typing___Text, PortLike]: ...

    @property
    def links(self) -> typing___MutableMapping[typing___Text, LinkLike]: ...

    @property
    def constraints(self) -> typing___MutableMapping[typing___Text, expr_pb2___ValueExpr]: ...

    @property
    def superclasses(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ref_pb2___LibraryPath]: ...

    @property
    def meta(self) -> common_pb2___Metadata: ...

    def __init__(self,
        *,
        params : typing___Optional[typing___Mapping[typing___Text, init_pb2___ValInit]] = None,
        ports : typing___Optional[typing___Mapping[typing___Text, PortLike]] = None,
        links : typing___Optional[typing___Mapping[typing___Text, LinkLike]] = None,
        constraints : typing___Optional[typing___Mapping[typing___Text, expr_pb2___ValueExpr]] = None,
        superclasses : typing___Optional[typing___Iterable[ref_pb2___LibraryPath]] = None,
        meta : typing___Optional[common_pb2___Metadata] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Link: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Link: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"meta",b"meta"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"constraints",b"constraints",u"links",b"links",u"meta",b"meta",u"params",b"params",u"ports",b"ports",u"superclasses",b"superclasses"]) -> None: ...

class LinkLike(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def undefined(self) -> common_pb2___Empty: ...

    @property
    def lib_elem(self) -> ref_pb2___LibraryPath: ...

    @property
    def link(self) -> Link: ...

    def __init__(self,
        *,
        undefined : typing___Optional[common_pb2___Empty] = None,
        lib_elem : typing___Optional[ref_pb2___LibraryPath] = None,
        link : typing___Optional[Link] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> LinkLike: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> LinkLike: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"lib_elem",b"lib_elem",u"link",b"link",u"type",b"type",u"undefined",b"undefined"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"lib_elem",b"lib_elem",u"link",b"link",u"type",b"type",u"undefined",b"undefined"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"type",b"type"]) -> typing_extensions___Literal["undefined","lib_elem","link"]: ...
