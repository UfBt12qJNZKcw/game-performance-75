import time
import functools
from typing import Callable, Any

def throttle(interval: float):
    def decorator(func: Callable):
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.perf_counter()
            if now - last_called[0] >= interval:
                last_called[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def memoize_frame(func: Callable):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

class PerformanceTimer:
    def __init__(self, label: str):
        self.label = label
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, *args):
        elapsed = (time.perf_counter() - self.start) * 1000
        print(f'[{self.label}] execution time: {elapsed:.3f}ms')

def clamp(val: float, min_val: float, max_val: float) -> float:
    return max(min_val, min(val, max_val))

def lerp(start: float, end: float, alpha: float) -> float:
    return start + (end - start) * clamp(alpha, 0.0, 1.0)