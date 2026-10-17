import functools
import time
import collections

class SmartCache:
    def __init__(self, ttl_seconds=30, max_size=128):
        self.ttl = ttl_seconds
        self.max_size = max_size
        self.cache = collections.OrderedDict()
        self.timestamps = {}

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()
            if key in self.cache and (now - self.timestamps.get(key, 0)) < self.ttl:
                return self.cache[key]
            
            result = func(*args, **kwargs)
            
            if len(self.cache) >= self.max_size:
                self.cache.popitem(last=False)
            
            self.cache[key] = result
            self.timestamps[key] = now
            return result
        return wrapper

    def invalidate(self):
        self.cache.clear()
        self.timestamps.clear()

    def batch_update(self, updates: dict):
        for key, value in updates.items():
            self.cache[key] = value
            self.timestamps[key] = time.time()

def optimized_compute(factor: float):
    """Pre-computes lookup table for heavy geometry shaders."""
    return {i: (i * factor) ** 0.5 for i in range(1024)}