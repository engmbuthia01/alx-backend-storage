#!/usr/bin/env python3
"""
This module contains a class
definition for Redis cache
"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    def __init__(self):
        """Initialize Redis client and flush database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis with a randomly generated key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable[[bytes], Union[str, int, float, bytes]]] = None
    ) -> Union[str, int, float, bytes, None]:
        """Retrieve data from Redis and optionally convert it using fn."""
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve data as a UTF-8 decoded string."""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve data as an integer."""
        return self.get(key, int)
