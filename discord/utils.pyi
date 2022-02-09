import datetime
from typing import Any, Callable, Optional, TypeVar, overload

T = TypeVar("T")
Epoch: int

class _Missing:
    @overload
    def __int__() -> int: ...
    @overload
    def __int__(self) -> None: ...
    @overload
    def __int__(self) -> None: ...
    def __bool__(self): ...
    def __eq__(self): ...

MISSING: Any

def copy_doc(original: Callable) -> Callable[[T], T]: ...
def utcnow(): ...
def create_snowflake(time: Optional[datetime.datetime] = ...) -> int: ...
async def getch(fetch, get) -> None: ...
def img_mime_type(data: bytes): ...
async def wait_for(futures, timeout): ...

class ExponentialBackoff:
    base: Any
    exp: int
    max: int
    reset_time: Any
    last_invoke: Any
    rand: Any
    def __init__(self, base: int = ..., *, integral: T = ...) -> None: ...
    def delay(self): ...