import io
import threading
from typing import Any

from .client import VoiceClient as VoiceClient

class AudioSource:
    def read(self) -> bytes: ...
    def is_opus(self) -> bool: ...
    def cleanup(self) -> None: ...
    def __del__(self) -> None: ...

class PCMAudio(AudioSource):
    stream: Any
    def __init__(self, stream: io.BufferedIOBase) -> None: ...
    def read(self) -> bytes: ...

class AudioPlayer(threading.Thread):
    DELAY: float
    daemon: bool
    source: Any
    client: Any
    after: Any
    end: Any
    resumed: Any
    error: Any
    connected: Any
    def __init__(
        self, source: AudioSource, client, *, after: Any | None = ...
    ) -> None: ...
    def run(self) -> None: ...
    def stop(self) -> None: ...
    def pause(self, *, update_speaking: bool = ...): ...
    loops: int
    start: Any
    def resume(self, *, update_speaking: bool = ...): ...