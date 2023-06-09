from __future__ import annotations

from .atomic import AtomicDict
from .patterns import singleton


@singleton
class AtomicMemorySession(AtomicDict):
    def __init__(self):
        super().__init__()


session = AtomicMemorySession()
