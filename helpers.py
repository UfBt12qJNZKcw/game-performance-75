import functools
import time
import collections

class JITCache:
    def __init__(self, limit=128):
        self.limit = limit
        self.storage = collections.OrderedDict()

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (func.__name__, args, frozenset(kwargs.items()))
            if key in self.storage:
                return self.storage[key]
            result = func(*args, **kwargs)
            if len(self.storage) >= self.limit:
                self.storage.popitem(last=False)
            self.storage[key] = result
            return result
        return wrapper

class LazyFrameTimer:
    def __init__(self, threshold=0.016):
        self.threshold = threshold
        self.last_tick = time.perf_counter()

    def throttle_frame_logic(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.perf_counter()
            if (now - self.last_tick) < self.threshold:
                return None
            self.last_tick = now
            return func(*args, **kwargs)
        return wrapper

def memory_compact_dispatch(data_dict):
    return {k: v for k, v in data_dict.items() if v is not None}