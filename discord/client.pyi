import asyncio
from typing import Any, Callable, List, Literal, Optional, TypeVar, Union

from discord.channels import VoiceChannel

from .ext.cogs import Cog
from .internal import dispatcher
from .state import ConnectionState
from .types.dict import Dict

CFT = TypeVar("CFT", bound="dispatcher.CoroFunc")

class Client:
    state: Any
    dispatcher: Any
    factory: Any
    application: Any
    gateway: Any
    cogs: Any
    chunk_guild_members: Any
    def __init__(
        self,
        loop: Optional[asyncio.AbstractEventLoop] = ...,
        intents: Optional[int] = ...,
        module: Optional[str] = ...,
        shards: Optional[int] = ...,
        mobile: Optional[bool] = ...,
        proxy: Optional[str] = ...,
        proxy_auth: Optional[str] = ...,
        logs: Optional[Union[None, int, str, Dict]] = ...,
        debug: Optional[bool] = ...,
        state: Optional[ConnectionState] = ...,
        chunk_guild_members: Optional[bool] = ...,
    ) -> None: ...
    token: Any
    async def login(self, token: str): ...
    def voice(self, channel: VoiceChannel): ...
    async def connect(self, token: str): ...
    def run(self, token: str): ...
    def fetch_guild(self, guild_id): ...
    def fetch_raw_guild(self, guild_id): ...
    async def get_guild(self, guild_id): ...
    async def get_voice_channel(self, channel_id: int): ...
    def create_button(
        self,
        label: str,
        callback: dispatcher.Coro,
        style: Literal[1, 2, 3, 4, 5] = ...,
        custom_id: str = ...,
        url: str = ...,
    ): ...
    @property
    def is_ready(self): ...
    @property
    def presence(self) -> list[str]: ...
    def change_presence(
        self,
        name: str,
        type: int,
        status: Literal["online", "dnd", "idle", "invisible", "offline"] = ...,
        stream_url: Optional[str] = ...,
        afk: Optional[bool] = ...,
    ): ...
    def event(self, coro: dispatcher.Coro) -> dispatcher.Coro: ...
    def listen(self, name: str = ...) -> Callable[[CFT], CFT]: ...
    @property
    def user(self): ...
    def slash_command(
        self,
        callback,
        name: str = ...,
        options: List[dict] = ...,
        guild_ids: List[int] = ...,
        description: str = ...,
        default_permission: bool = ...,
    ): ...
    def add_cog(self, cog: Cog, *, override: bool = ...): ...
    def remove_cog(self, cog: Cog): ...
    def add_extension(self, name: str, *, package: Optional[str] = ...): ...
    def remove_extension(self, name: str, *, package: Optional[str] = ...): ...