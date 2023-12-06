from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Data(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[_Iterable[str]] = ...) -> None: ...

class JsonFileRequest(_message.Message):
    __slots__ = ["filename", "title", "data"]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    filename: str
    title: _containers.RepeatedScalarFieldContainer[str]
    data: _containers.RepeatedCompositeFieldContainer[Data]
    def __init__(self, filename: _Optional[str] = ..., title: _Optional[_Iterable[str]] = ..., data: _Optional[_Iterable[_Union[Data, _Mapping]]] = ...) -> None: ...

class ExcelFileReply(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: bytes
    def __init__(self, message: _Optional[bytes] = ...) -> None: ...
