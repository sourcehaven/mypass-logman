from __future__ import annotations


def singleton(clazz):
    # noinspection PyUnusedLocal
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance') or cls._instance is None:
            cls._instance = super(cls, cls).__new__(cls)
        return cls._instance

    clazz.__new__ = __new__
    return clazz
