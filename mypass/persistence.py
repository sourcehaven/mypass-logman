from __future__ import annotations

from .atomic import AtomicDict
from .patterns import singleton
from .exceptions import MissingSessionKeyError


@singleton
class AtomicMemorySession(AtomicDict):
    def __init__(self):
        super().__init__()

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except KeyError as e:
            raise MissingSessionKeyError(*e.args)


session = AtomicMemorySession()
