import gc
import time
import psutil
import functools

def memory_cleanup_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        gc.collect()
        return result
    return wrapper

def get_system_metrics():
    proc = psutil.Process()
    return {
        "rss": proc.memory_info().rss / 1024 / 1024,
        "cpu": proc.cpu_percent(interval=0.1),
        "timestamp": time.time()
    }

class ResourcePool:
    def __init__(self, limit=100):
        self._limit = limit
        self._cache = {}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.purge()

    def register(self, key, obj):
        if len(self._cache) >= self._limit:
            self.purge()
        self._cache[key] = obj

    def purge(self):
        keys = list(self._cache.keys())
        for key in keys:
            del self._cache[key]
        gc.collect()

cleanup = memory_cleanup_decorator