#!/usr/bin/env python3
"""
This module contains a class
definition for Redis cache
"""

import redis
import uuid
from typing import Union, Callable, Optional, Any
import functools


def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a method is called."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        Wrapped function that increments the
        call counter and calls the original method
        """
        # Use the method's qualified name as the Redis key
        key = method.__qualname__

        # Increment the call count for this method in Redis
        self._redis.incr(key)

        # Call the original method and return its result
        return method(self, *args, **kwargs)

    return wrapper

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
