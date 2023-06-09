from __future__ import annotations

from multiprocessing import Lock


class Lockable:
    def __init__(self):
        self._lock = Lock()


class AtomicSet(Lockable):
    def __init__(self):
        super().__init__()
        self._set = set()

    def __contains__(self, item):
        return item in self._set

    def __str__(self):
        return str(self._set)

    def __repr__(self):
        return str(self)

    def add(self, element):
        with self._lock:
            return self._set.add(element)

    def pop(self):
        with self._lock:
            return self._set.pop()

    def remove(self, element):
        with self._lock:
            return self._set.remove(element)

    def clear(self):
        with self._lock:
            return self._set.clear()


class AtomicDict(Lockable):
    def __init__(self):
        super().__init__()
        self._dict = {}

    def __contains__(self, item):
        return item in self._dict

    def __getitem__(self, k):
        return self._dict[k]

    def __setitem__(self, k, v):
        with self._lock:
            self._dict[k] = v

    def __delitem__(self, k):
        with self._lock:
            del self._dict[k]

    def __str__(self):
        return str(self._dict)

    def __repr__(self):
        return str(self)

    def get(self, __key, __default):
        return self._dict.get(__key, __default)

    def pop(self, __key):
        with self._lock:
            return self._dict.pop(__key)

    def clear(self):
        with self._lock:
            return self._dict.clear()
