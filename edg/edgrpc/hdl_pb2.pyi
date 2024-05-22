"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
* Defines messages for a service provided in Python that exposes
HDL-to-edgir elaboration for a compiler in a different process / language.
"""
import builtins
import collections.abc
from .. import edgir
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import typing
if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Refinements(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Subclass(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        PATH_FIELD_NUMBER: builtins.int
        CLS_FIELD_NUMBER: builtins.int
        REPLACEMENT_FIELD_NUMBER: builtins.int

        @property
        def path(self) -> edgir.ref_pb2.LocalPath:
            ...

        @property
        def cls(self) -> edgir.ref_pb2.LibraryPath:
            ...

        @property
        def replacement(self) -> edgir.ref_pb2.LibraryPath:
            ...

        def __init__(self, *, path: edgir.ref_pb2.LocalPath | None=..., cls: edgir.ref_pb2.LibraryPath | None=..., replacement: edgir.ref_pb2.LibraryPath | None=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['cls', b'cls', 'path', b'path', 'replacement', b'replacement', 'source', b'source']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['cls', b'cls', 'path', b'path', 'replacement', b'replacement', 'source', b'source']) -> None:
            ...

        def WhichOneof(self, oneof_group: typing_extensions.Literal['source', b'source']) -> typing_extensions.Literal['path', 'cls'] | None:
            ...

    @typing_extensions.final
    class Value(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        @typing_extensions.final
        class ClassParamPath(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            CLS_FIELD_NUMBER: builtins.int
            PARAM_PATH_FIELD_NUMBER: builtins.int

            @property
            def cls(self) -> edgir.ref_pb2.LibraryPath:
                ...

            @property
            def param_path(self) -> edgir.ref_pb2.LocalPath:
                ...

            def __init__(self, *, cls: edgir.ref_pb2.LibraryPath | None=..., param_path: edgir.ref_pb2.LocalPath | None=...) -> None:
                ...

            def HasField(self, field_name: typing_extensions.Literal['cls', b'cls', 'param_path', b'param_path']) -> builtins.bool:
                ...

            def ClearField(self, field_name: typing_extensions.Literal['cls', b'cls', 'param_path', b'param_path']) -> None:
                ...
        PATH_FIELD_NUMBER: builtins.int
        CLS_PARAM_FIELD_NUMBER: builtins.int
        EXPR_FIELD_NUMBER: builtins.int
        PARAM_FIELD_NUMBER: builtins.int

        @property
        def path(self) -> edgir.ref_pb2.LocalPath:
            ...

        @property
        def cls_param(self) -> global___Refinements.Value.ClassParamPath:
            ...

        @property
        def expr(self) -> edgir.lit_pb2.ValueLit:
            """set to a specific value"""

        @property
        def param(self) -> edgir.ref_pb2.LocalPath:
            """set to a value of another parameter - invalid for classes for now"""

        def __init__(self, *, path: edgir.ref_pb2.LocalPath | None=..., cls_param: global___Refinements.Value.ClassParamPath | None=..., expr: edgir.lit_pb2.ValueLit | None=..., param: edgir.ref_pb2.LocalPath | None=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['cls_param', b'cls_param', 'expr', b'expr', 'param', b'param', 'path', b'path', 'source', b'source', 'value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['cls_param', b'cls_param', 'expr', b'expr', 'param', b'param', 'path', b'path', 'source', b'source', 'value', b'value']) -> None:
            ...

        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal['source', b'source']) -> typing_extensions.Literal['path', 'cls_param'] | None:
            ...

        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal['value', b'value']) -> typing_extensions.Literal['expr', 'param'] | None:
            ...
    SUBCLASSES_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int

    @property
    def subclasses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Refinements.Subclass]:
        ...

    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Refinements.Value]:
        ...

    def __init__(self, *, subclasses: collections.abc.Iterable[global___Refinements.Subclass] | None=..., values: collections.abc.Iterable[global___Refinements.Value] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['subclasses', b'subclasses', 'values', b'values']) -> None:
        ...
global___Refinements = Refinements

@typing_extensions.final
class ModuleName(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___ModuleName = ModuleName

@typing_extensions.final
class IndexResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INDEXED_FIELD_NUMBER: builtins.int

    @property
    def indexed(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[edgir.ref_pb2.LibraryPath]:
        ...

    def __init__(self, *, indexed: collections.abc.Iterable[edgir.ref_pb2.LibraryPath] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['indexed', b'indexed']) -> None:
        ...
global___IndexResponse = IndexResponse

@typing_extensions.final
class LibraryRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ELEMENT_FIELD_NUMBER: builtins.int

    @property
    def element(self) -> edgir.ref_pb2.LibraryPath:
        """library element asked for"""

    def __init__(self, *, element: edgir.ref_pb2.LibraryPath | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['element', b'element']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['element', b'element']) -> None:
        ...
global___LibraryRequest = LibraryRequest

@typing_extensions.final
class LibraryResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ELEMENT_FIELD_NUMBER: builtins.int
    REFINEMENTS_FIELD_NUMBER: builtins.int

    @property
    def element(self) -> edgir.schema_pb2.Library.NS.Val:
        ...

    @property
    def refinements(self) -> global___Refinements:
        """only valid if element is a top-level block"""

    def __init__(self, *, element: edgir.schema_pb2.Library.NS.Val | None=..., refinements: global___Refinements | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['element', b'element', 'refinements', b'refinements']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['element', b'element', 'refinements', b'refinements']) -> None:
        ...
global___LibraryResponse = LibraryResponse

@typing_extensions.final
class ExprValue(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PATH_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int

    @property
    def path(self) -> edgir.ref_pb2.LocalPath:
        ...

    @property
    def value(self) -> edgir.lit_pb2.ValueLit:
        ...

    def __init__(self, *, path: edgir.ref_pb2.LocalPath | None=..., value: edgir.lit_pb2.ValueLit | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['path', b'path', 'value', b'value']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['path', b'path', 'value', b'value']) -> None:
        ...
global___ExprValue = ExprValue

@typing_extensions.final
class GeneratorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ELEMENT_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int

    @property
    def element(self) -> edgir.ref_pb2.LibraryPath:
        """path of library element containing the generator"""

    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ExprValue]:
        ...

    def __init__(self, *, element: edgir.ref_pb2.LibraryPath | None=..., values: collections.abc.Iterable[global___ExprValue] | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['element', b'element']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['element', b'element', 'values', b'values']) -> None:
        ...
global___GeneratorRequest = GeneratorRequest

@typing_extensions.final
class GeneratorResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GENERATED_FIELD_NUMBER: builtins.int

    @property
    def generated(self) -> edgir.elem_pb2.HierarchyBlock:
        ...

    def __init__(self, *, generated: edgir.elem_pb2.HierarchyBlock | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['generated', b'generated']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['generated', b'generated']) -> None:
        ...
global___GeneratorResponse = GeneratorResponse

@typing_extensions.final
class RefinementRequest(google.protobuf.message.Message):
    """Runs a refinement pass - something that takes a full design and solved values and
    generates additional values, eg for refdes assignment
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REFINEMENT_PASS_FIELD_NUMBER: builtins.int
    DESIGN_FIELD_NUMBER: builtins.int
    SOLVEDVALUES_FIELD_NUMBER: builtins.int

    @property
    def refinement_pass(self) -> edgir.ref_pb2.LibraryPath:
        ...

    @property
    def design(self) -> edgir.schema_pb2.Design:
        ...

    @property
    def solvedValues(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ExprValue]:
        ...

    def __init__(self, *, refinement_pass: edgir.ref_pb2.LibraryPath | None=..., design: edgir.schema_pb2.Design | None=..., solvedValues: collections.abc.Iterable[global___ExprValue] | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['design', b'design', 'refinement_pass', b'refinement_pass']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['design', b'design', 'refinement_pass', b'refinement_pass', 'solvedValues', b'solvedValues']) -> None:
        ...
global___RefinementRequest = RefinementRequest

@typing_extensions.final
class RefinementResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NEWVALUES_FIELD_NUMBER: builtins.int

    @property
    def newValues(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ExprValue]:
        ...

    def __init__(self, *, newValues: collections.abc.Iterable[global___ExprValue] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['newValues', b'newValues']) -> None:
        ...
global___RefinementResponse = RefinementResponse

@typing_extensions.final
class BackendRequest(google.protobuf.message.Message):
    """Runs a backend - something that generates fabrication artifacts from a compiled design tree
    eg, generate KiCad netlist, or generate microcontroller firmware pinmap headers
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ArgumentsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str

        def __init__(self, *, key: builtins.str=..., value: builtins.str=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...
    BACKEND_FIELD_NUMBER: builtins.int
    DESIGN_FIELD_NUMBER: builtins.int
    SOLVEDVALUES_FIELD_NUMBER: builtins.int
    ARGUMENTS_FIELD_NUMBER: builtins.int

    @property
    def backend(self) -> edgir.ref_pb2.LibraryPath:
        ...

    @property
    def design(self) -> edgir.schema_pb2.Design:
        ...

    @property
    def solvedValues(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ExprValue]:
        ...

    @property
    def arguments(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        ...

    def __init__(self, *, backend: edgir.ref_pb2.LibraryPath | None=..., design: edgir.schema_pb2.Design | None=..., solvedValues: collections.abc.Iterable[global___ExprValue] | None=..., arguments: collections.abc.Mapping[builtins.str, builtins.str] | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['backend', b'backend', 'design', b'design']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['arguments', b'arguments', 'backend', b'backend', 'design', b'design', 'solvedValues', b'solvedValues']) -> None:
        ...
global___BackendRequest = BackendRequest

@typing_extensions.final
class BackendResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Result(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        PATH_FIELD_NUMBER: builtins.int
        TEXT_FIELD_NUMBER: builtins.int

        @property
        def path(self) -> edgir.ref_pb2.LocalPath:
            """path of corresponding element in design tree"""
        text: builtins.str
        'for now, only text supported, for KiCad netlisting'

        def __init__(self, *, path: edgir.ref_pb2.LocalPath | None=..., text: builtins.str=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['path', b'path', 'result', b'result', 'text', b'text']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['path', b'path', 'result', b'result', 'text', b'text']) -> None:
            ...

        def WhichOneof(self, oneof_group: typing_extensions.Literal['result', b'result']) -> typing_extensions.Literal['text'] | None:
            ...
    RESULTS_FIELD_NUMBER: builtins.int

    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BackendResponse.Result]:
        ...

    def __init__(self, *, results: collections.abc.Iterable[global___BackendResponse.Result] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['results', b'results']) -> None:
        ...
global___BackendResponse = BackendResponse

@typing_extensions.final
class ErrorResponse(google.protobuf.message.Message):
    """catch all error response"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ERROR_FIELD_NUMBER: builtins.int
    TRACEBACK_FIELD_NUMBER: builtins.int
    error: builtins.str
    traceback: builtins.str

    def __init__(self, *, error: builtins.str=..., traceback: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['error', b'error', 'traceback', b'traceback']) -> None:
        ...
global___ErrorResponse = ErrorResponse

@typing_extensions.final
class HdlRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INDEX_MODULE_FIELD_NUMBER: builtins.int
    GET_LIBRARY_ELEMENT_FIELD_NUMBER: builtins.int
    ELABORATE_GENERATOR_FIELD_NUMBER: builtins.int
    RUN_REFINEMENT_FIELD_NUMBER: builtins.int
    RUN_BACKEND_FIELD_NUMBER: builtins.int
    GET_PROTO_VERSION_FIELD_NUMBER: builtins.int

    @property
    def index_module(self) -> global___ModuleName:
        """returns an index of IR elements in a Python module"""

    @property
    def get_library_element(self) -> global___LibraryRequest:
        """returns the IR for a library element"""

    @property
    def elaborate_generator(self) -> global___GeneratorRequest:
        """returns the elaborated IR"""

    @property
    def run_refinement(self) -> global___RefinementRequest:
        ...

    @property
    def run_backend(self) -> global___BackendRequest:
        ...
    get_proto_version: builtins.int
    'no data'

    def __init__(self, *, index_module: global___ModuleName | None=..., get_library_element: global___LibraryRequest | None=..., elaborate_generator: global___GeneratorRequest | None=..., run_refinement: global___RefinementRequest | None=..., run_backend: global___BackendRequest | None=..., get_proto_version: builtins.int=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['elaborate_generator', b'elaborate_generator', 'get_library_element', b'get_library_element', 'get_proto_version', b'get_proto_version', 'index_module', b'index_module', 'request', b'request', 'run_backend', b'run_backend', 'run_refinement', b'run_refinement']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['elaborate_generator', b'elaborate_generator', 'get_library_element', b'get_library_element', 'get_proto_version', b'get_proto_version', 'index_module', b'index_module', 'request', b'request', 'run_backend', b'run_backend', 'run_refinement', b'run_refinement']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['request', b'request']) -> typing_extensions.Literal['index_module', 'get_library_element', 'elaborate_generator', 'run_refinement', 'run_backend', 'get_proto_version'] | None:
        ...
global___HdlRequest = HdlRequest

@typing_extensions.final
class HdlResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INDEX_MODULE_FIELD_NUMBER: builtins.int
    GET_LIBRARY_ELEMENT_FIELD_NUMBER: builtins.int
    ELABORATE_GENERATOR_FIELD_NUMBER: builtins.int
    RUN_REFINEMENT_FIELD_NUMBER: builtins.int
    RUN_BACKEND_FIELD_NUMBER: builtins.int
    GET_PROTO_VERSION_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int

    @property
    def index_module(self) -> global___IndexResponse:
        """list of contained library elements"""

    @property
    def get_library_element(self) -> global___LibraryResponse:
        ...

    @property
    def elaborate_generator(self) -> global___GeneratorResponse:
        ...

    @property
    def run_refinement(self) -> global___RefinementResponse:
        ...

    @property
    def run_backend(self) -> global___BackendResponse:
        ...
    get_proto_version: builtins.int

    @property
    def error(self) -> global___ErrorResponse:
        ...

    def __init__(self, *, index_module: global___IndexResponse | None=..., get_library_element: global___LibraryResponse | None=..., elaborate_generator: global___GeneratorResponse | None=..., run_refinement: global___RefinementResponse | None=..., run_backend: global___BackendResponse | None=..., get_proto_version: builtins.int=..., error: global___ErrorResponse | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['elaborate_generator', b'elaborate_generator', 'error', b'error', 'get_library_element', b'get_library_element', 'get_proto_version', b'get_proto_version', 'index_module', b'index_module', 'response', b'response', 'run_backend', b'run_backend', 'run_refinement', b'run_refinement']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['elaborate_generator', b'elaborate_generator', 'error', b'error', 'get_library_element', b'get_library_element', 'get_proto_version', b'get_proto_version', 'index_module', b'index_module', 'response', b'response', 'run_backend', b'run_backend', 'run_refinement', b'run_refinement']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['response', b'response']) -> typing_extensions.Literal['index_module', 'get_library_element', 'elaborate_generator', 'run_refinement', 'run_backend', 'get_proto_version', 'error'] | None:
        ...
global___HdlResponse = HdlResponse