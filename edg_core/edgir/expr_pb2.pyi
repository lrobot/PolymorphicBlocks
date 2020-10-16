# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from .common_pb2 import (
    Metadata as common_pb2___Metadata,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from .lit_pb2 import (
    ValueLit as lit_pb2___ValueLit,
)

from .ref_pb2 import (
    LocalPath as ref_pb2___LocalPath,
)

from typing import (
    List as typing___List,
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    Union as typing___Union,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class BinaryExpr(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Op(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'BinaryExpr.Op': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['BinaryExpr.Op']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'BinaryExpr.Op']]: ...
        UNDEFINED = typing___cast('BinaryExpr.Op', 0)
        ADD = typing___cast('BinaryExpr.Op', 10)
        SUB = typing___cast('BinaryExpr.Op', 11)
        MULT = typing___cast('BinaryExpr.Op', 12)
        DIV = typing___cast('BinaryExpr.Op', 13)
        AND = typing___cast('BinaryExpr.Op', 20)
        OR = typing___cast('BinaryExpr.Op', 21)
        XOR = typing___cast('BinaryExpr.Op', 22)
        IMPLIES = typing___cast('BinaryExpr.Op', 23)
        EQ = typing___cast('BinaryExpr.Op', 30)
        NEQ = typing___cast('BinaryExpr.Op', 31)
        GT = typing___cast('BinaryExpr.Op', 40)
        GTE = typing___cast('BinaryExpr.Op', 41)
        LT = typing___cast('BinaryExpr.Op', 42)
        LTE = typing___cast('BinaryExpr.Op', 44)
        MAX = typing___cast('BinaryExpr.Op', 45)
        MIN = typing___cast('BinaryExpr.Op', 46)
        INTERSECTION = typing___cast('BinaryExpr.Op', 51)
        SUBSET = typing___cast('BinaryExpr.Op', 53)
        RANGE = typing___cast('BinaryExpr.Op', 1)
    UNDEFINED = typing___cast('BinaryExpr.Op', 0)
    ADD = typing___cast('BinaryExpr.Op', 10)
    SUB = typing___cast('BinaryExpr.Op', 11)
    MULT = typing___cast('BinaryExpr.Op', 12)
    DIV = typing___cast('BinaryExpr.Op', 13)
    AND = typing___cast('BinaryExpr.Op', 20)
    OR = typing___cast('BinaryExpr.Op', 21)
    XOR = typing___cast('BinaryExpr.Op', 22)
    IMPLIES = typing___cast('BinaryExpr.Op', 23)
    EQ = typing___cast('BinaryExpr.Op', 30)
    NEQ = typing___cast('BinaryExpr.Op', 31)
    GT = typing___cast('BinaryExpr.Op', 40)
    GTE = typing___cast('BinaryExpr.Op', 41)
    LT = typing___cast('BinaryExpr.Op', 42)
    LTE = typing___cast('BinaryExpr.Op', 44)
    MAX = typing___cast('BinaryExpr.Op', 45)
    MIN = typing___cast('BinaryExpr.Op', 46)
    INTERSECTION = typing___cast('BinaryExpr.Op', 51)
    SUBSET = typing___cast('BinaryExpr.Op', 53)
    RANGE = typing___cast('BinaryExpr.Op', 1)

    op = ... # type: BinaryExpr.Op

    @property
    def lhs(self) -> ValueExpr: ...

    @property
    def rhs(self) -> ValueExpr: ...

    def __init__(self,
        *,
        op : typing___Optional[BinaryExpr.Op] = None,
        lhs : typing___Optional[ValueExpr] = None,
        rhs : typing___Optional[ValueExpr] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> BinaryExpr: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> BinaryExpr: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"lhs",b"lhs",u"rhs",b"rhs"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"lhs",b"lhs",u"op",b"op",u"rhs",b"rhs"]) -> None: ...

class ReductionExpr(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Op(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'ReductionExpr.Op': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['ReductionExpr.Op']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'ReductionExpr.Op']]: ...
        UNDEFINED = typing___cast('ReductionExpr.Op', 0)
        SUM = typing___cast('ReductionExpr.Op', 1)
        ALL_TRUE = typing___cast('ReductionExpr.Op', 2)
        ANY_TRUE = typing___cast('ReductionExpr.Op', 3)
        ALL_EQ = typing___cast('ReductionExpr.Op', 4)
        ALL_UNIQUE = typing___cast('ReductionExpr.Op', 5)
        MAXIMUM = typing___cast('ReductionExpr.Op', 10)
        MINIMUM = typing___cast('ReductionExpr.Op', 11)
        SET_EXTRACT = typing___cast('ReductionExpr.Op', 12)
        INTERSECTION = typing___cast('ReductionExpr.Op', 13)
    UNDEFINED = typing___cast('ReductionExpr.Op', 0)
    SUM = typing___cast('ReductionExpr.Op', 1)
    ALL_TRUE = typing___cast('ReductionExpr.Op', 2)
    ANY_TRUE = typing___cast('ReductionExpr.Op', 3)
    ALL_EQ = typing___cast('ReductionExpr.Op', 4)
    ALL_UNIQUE = typing___cast('ReductionExpr.Op', 5)
    MAXIMUM = typing___cast('ReductionExpr.Op', 10)
    MINIMUM = typing___cast('ReductionExpr.Op', 11)
    SET_EXTRACT = typing___cast('ReductionExpr.Op', 12)
    INTERSECTION = typing___cast('ReductionExpr.Op', 13)

    op = ... # type: ReductionExpr.Op

    @property
    def vals(self) -> ValueExpr: ...

    def __init__(self,
        *,
        op : typing___Optional[ReductionExpr.Op] = None,
        vals : typing___Optional[ValueExpr] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ReductionExpr: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ReductionExpr: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"vals",b"vals"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"op",b"op",u"vals",b"vals"]) -> None: ...

class RangeExpr(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def minimum(self) -> ValueExpr: ...

    @property
    def maximum(self) -> ValueExpr: ...

    def __init__(self,
        *,
        minimum : typing___Optional[ValueExpr] = None,
        maximum : typing___Optional[ValueExpr] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> RangeExpr: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> RangeExpr: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"maximum",b"maximum",u"minimum",b"minimum"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"maximum",b"maximum",u"minimum",b"minimum"]) -> None: ...

class StructExpr(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ValsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> ValueExpr: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[ValueExpr] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> StructExpr.ValsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StructExpr.ValsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...


    @property
    def vals(self) -> typing___MutableMapping[typing___Text, ValueExpr]: ...

    def __init__(self,
        *,
        vals : typing___Optional[typing___Mapping[typing___Text, ValueExpr]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> StructExpr: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StructExpr: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"vals",b"vals"]) -> None: ...

class IfThenElseExpr(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def cond(self) -> ValueExpr: ...

    @property
    def tru(self) -> ValueExpr: ...

    @property
    def fal(self) -> ValueExpr: ...

    @property
    def meta(self) -> common_pb2___Metadata: ...

    def __init__(self,
        *,
        cond : typing___Optional[ValueExpr] = None,
        tru : typing___Optional[ValueExpr] = None,
        fal : typing___Optional[ValueExpr] = None,
        meta : typing___Optional[common_pb2___Metadata] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> IfThenElseExpr: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> IfThenElseExpr: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"cond",b"cond",u"fal",b"fal",u"meta",b"meta",u"tru",b"tru"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"cond",b"cond",u"fal",b"fal",u"meta",b"meta",u"tru",b"tru"]) -> None: ...

class ExtractExpr(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def container(self) -> ValueExpr: ...

    @property
    def index(self) -> ValueExpr: ...

    def __init__(self,
        *,
        container : typing___Optional[ValueExpr] = None,
        index : typing___Optional[ValueExpr] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ExtractExpr: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExtractExpr: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"container",b"container",u"index",b"index"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"container",b"container",u"index",b"index"]) -> None: ...

class MapExtractExpr(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def container(self) -> ValueExpr: ...

    @property
    def path(self) -> ref_pb2___LocalPath: ...

    def __init__(self,
        *,
        container : typing___Optional[ValueExpr] = None,
        path : typing___Optional[ref_pb2___LocalPath] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MapExtractExpr: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> MapExtractExpr: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"container",b"container",u"path",b"path"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"container",b"container",u"path",b"path"]) -> None: ...

class ConnectedExpr(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def block_port(self) -> ValueExpr: ...

    @property
    def link_port(self) -> ValueExpr: ...

    def __init__(self,
        *,
        block_port : typing___Optional[ValueExpr] = None,
        link_port : typing___Optional[ValueExpr] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ConnectedExpr: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ConnectedExpr: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"block_port",b"block_port",u"link_port",b"link_port"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"block_port",b"block_port",u"link_port",b"link_port"]) -> None: ...

class ExportedExpr(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def exterior_port(self) -> ValueExpr: ...

    @property
    def internal_block_port(self) -> ValueExpr: ...

    def __init__(self,
        *,
        exterior_port : typing___Optional[ValueExpr] = None,
        internal_block_port : typing___Optional[ValueExpr] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ExportedExpr: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExportedExpr: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"exterior_port",b"exterior_port",u"internal_block_port",b"internal_block_port"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"exterior_port",b"exterior_port",u"internal_block_port",b"internal_block_port"]) -> None: ...

class ValueExpr(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def literal(self) -> lit_pb2___ValueLit: ...

    @property
    def binary(self) -> BinaryExpr: ...

    @property
    def reduce(self) -> ReductionExpr: ...

    @property
    def struct(self) -> StructExpr: ...

    @property
    def range(self) -> RangeExpr: ...

    @property
    def ifThenElse(self) -> IfThenElseExpr: ...

    @property
    def extract(self) -> ExtractExpr: ...

    @property
    def map_extract(self) -> MapExtractExpr: ...

    @property
    def connected(self) -> ConnectedExpr: ...

    @property
    def exported(self) -> ExportedExpr: ...

    @property
    def ref(self) -> ref_pb2___LocalPath: ...

    @property
    def meta(self) -> common_pb2___Metadata: ...

    def __init__(self,
        *,
        literal : typing___Optional[lit_pb2___ValueLit] = None,
        binary : typing___Optional[BinaryExpr] = None,
        reduce : typing___Optional[ReductionExpr] = None,
        struct : typing___Optional[StructExpr] = None,
        range : typing___Optional[RangeExpr] = None,
        ifThenElse : typing___Optional[IfThenElseExpr] = None,
        extract : typing___Optional[ExtractExpr] = None,
        map_extract : typing___Optional[MapExtractExpr] = None,
        connected : typing___Optional[ConnectedExpr] = None,
        exported : typing___Optional[ExportedExpr] = None,
        ref : typing___Optional[ref_pb2___LocalPath] = None,
        meta : typing___Optional[common_pb2___Metadata] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ValueExpr: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ValueExpr: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"binary",b"binary",u"connected",b"connected",u"exported",b"exported",u"expr",b"expr",u"extract",b"extract",u"ifThenElse",b"ifThenElse",u"literal",b"literal",u"map_extract",b"map_extract",u"meta",b"meta",u"range",b"range",u"reduce",b"reduce",u"ref",b"ref",u"struct",b"struct"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"binary",b"binary",u"connected",b"connected",u"exported",b"exported",u"expr",b"expr",u"extract",b"extract",u"ifThenElse",b"ifThenElse",u"literal",b"literal",u"map_extract",b"map_extract",u"meta",b"meta",u"range",b"range",u"reduce",b"reduce",u"ref",b"ref",u"struct",b"struct"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"expr",b"expr"]) -> typing_extensions___Literal["literal","binary","reduce","struct","range","ifThenElse","extract","map_extract","connected","exported","ref"]: ...
