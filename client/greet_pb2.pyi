from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Iterable as _Iterable,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class GameRequest(_message.Message):
    __slots__ = ("game",)
    GAME_FIELD_NUMBER: _ClassVar[int]
    game: str
    def __init__(self, game: _Optional[str] = ...) -> None: ...

class ConsoleRequest(_message.Message):
    __slots__ = ("game", "console")
    GAME_FIELD_NUMBER: _ClassVar[int]
    CONSOLE_FIELD_NUMBER: _ClassVar[int]
    game: str
    console: str
    def __init__(
        self, game: _Optional[str] = ..., console: _Optional[str] = ...
    ) -> None: ...

class GameReply(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class GamesReply(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _containers.RepeatedCompositeFieldContainer[GameReply]
    def __init__(
        self, message: _Optional[_Iterable[_Union[GameReply, _Mapping]]] = ...
    ) -> None: ...
