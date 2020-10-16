# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from .common_pb2 import (
    Metadata as common_pb2___Metadata,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from .name_pb2 import (
    LibraryName as name_pb2___LibraryName,
    Namespace as name_pb2___Namespace,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
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


class Reserved(builtin___int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: builtin___int) -> builtin___str: ...
    @classmethod
    def Value(cls, name: builtin___str) -> 'Reserved': ...
    @classmethod
    def keys(cls) -> typing___List[builtin___str]: ...
    @classmethod
    def values(cls) -> typing___List['Reserved']: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[builtin___str, 'Reserved']]: ...
    UNDEFINED = typing___cast('Reserved', 0)
    CONNECTED_LINK = typing___cast('Reserved', 1)
    IS_CONNECTED = typing___cast('Reserved', 40)
UNDEFINED = typing___cast('Reserved', 0)
CONNECTED_LINK = typing___cast('Reserved', 1)
IS_CONNECTED = typing___cast('Reserved', 40)

class LocalStep(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    reserved_param = ... # type: Reserved
    name = ... # type: typing___Text

    def __init__(self,
        *,
        reserved_param : typing___Optional[Reserved] = None,
        name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> LocalStep: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> LocalStep: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"name",b"name",u"reserved_param",b"reserved_param",u"step",b"step"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name",u"reserved_param",b"reserved_param",u"step",b"step"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"step",b"step"]) -> typing_extensions___Literal["reserved_param","name"]: ...

class LocalPath(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def steps(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[LocalStep]: ...

    @property
    def meta(self) -> common_pb2___Metadata: ...

    def __init__(self,
        *,
        steps : typing___Optional[typing___Iterable[LocalStep]] = None,
        meta : typing___Optional[common_pb2___Metadata] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> LocalPath: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> LocalPath: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"meta",b"meta"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"meta",b"meta",u"steps",b"steps"]) -> None: ...

class LibraryPath(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def start(self) -> name_pb2___LibraryName: ...

    @property
    def steps(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[name_pb2___Namespace]: ...

    @property
    def target(self) -> LocalStep: ...

    @property
    def meta(self) -> common_pb2___Metadata: ...

    def __init__(self,
        *,
        start : typing___Optional[name_pb2___LibraryName] = None,
        steps : typing___Optional[typing___Iterable[name_pb2___Namespace]] = None,
        target : typing___Optional[LocalStep] = None,
        meta : typing___Optional[common_pb2___Metadata] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> LibraryPath: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> LibraryPath: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"meta",b"meta",u"start",b"start",u"target",b"target"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"meta",b"meta",u"start",b"start",u"steps",b"steps",u"target",b"target"]) -> None: ...
