from typing import Any, Union

from .enums import FormatType as FormatType
from .guild import Guild as Guild
from .state import ConnectionState as ConnectionState
from .user import User as User

def channel_parse(type: int, data: dict, state: ConnectionState): ...

class Category:
    from_dict: Any
    state: Any
    def __init__(self, data: dict, state: ConnectionState) -> None: ...
    def permission_overwrites(self) -> list[str, Union[int, str]]: ...
    @property
    def position(self) -> int: ...
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...
    def guild_id(self) -> int: ...

class TextChannel:
    from_dict: Any
    state: Any
    def __init__(self, data: dict, state: ConnectionState) -> None: ...
    @property
    def id(self) -> int: ...
    @property
    def guild_id(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def position(self) -> int: ...
    def permission_overwrites(self) -> list[str, Union[int, str]]: ...
    @property
    def nsfw(self) -> bool: ...
    def topic(self) -> str: ...
    def last_message_id(self) -> int: ...
    def category_id(self) -> int: ...

class VoiceChannel:
    state: Any
    from_dict: Any
    def __init__(self, data: dict, state: ConnectionState) -> None: ...
    @property
    def id(self) -> int: ...
    @property
    def guild(self) -> Guild: ...
    @property
    def name(self) -> str: ...
    @property
    def position(self) -> int: ...
    def permission_overwrites(self) -> list[str, Union[int, str]]: ...

class DMChannel:
    from_dict: Any
    state: Any
    def __init__(self, data: dict, state: ConnectionState) -> None: ...
    def last_message_id(self) -> int: ...
    @property
    def id(self) -> int: ...
    def recipients(self): ...

def parse_groupdm_icon(
    format: FormatType, group_id: int, group_icon_hash: str
) -> str: ...

class GroupDMChannel(DMChannel):
    def name(self) -> str: ...
    def icon(self, format: FormatType = ...) -> str: ...
    def owner(self) -> User: ...

class Thread:
    from_dict: Any
    state: Any
    def __init__(self, data: dict, state: ConnectionState) -> None: ...
    @property
    def id(self) -> int: ...
    @property
    def guild_id(self) -> int: ...
    @property
    def channel_id(self) -> int: ...
    @property
    def owner_id(self) -> int: ...
    @property
    def name(self) -> str: ...
    def last_message_id(self) -> int: ...
    def message_count(self) -> int: ...
    def member_count(self) -> int: ...
    @property
    def metadata(self) -> ThreadMetadata: ...

class ThreadMetadata:
    from_dict: Any
    def __init__(self, data: dict) -> None: ...
    @property
    def archived(self) -> bool: ...
    @property
    def auto_archive_duration(self) -> int: ...
    @property
    def archive_timestamp(self) -> str: ...
    @property
    def locked(self) -> bool: ...