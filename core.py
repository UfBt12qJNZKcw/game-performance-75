import time
import functools
from typing import Callable, Any

def frame_throttle(ms: int = 16):
    def decorator(func: Callable):
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.perf_counter()
            if (now - last_called[0]) * 1000 >= ms:
                last_called[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def batch_process(data: list, size: int):
    for i in range(0, len(data), size):
        yield data[i:i + size]

def memoize_per_frame(func: Callable):
    cache = {}
    def clear_cache():
        cache.clear()
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper.clear = clear_cache
    return wrapper

class EntityPool:
    def __init__(self, factory: Callable):
        self._pool = []
        self._factory = factory
    def acquire(self) -> Any:
        return self._pool.pop() if self._pool else self._factory()
    def release(self, obj: Any):
        self._pool.append(obj)