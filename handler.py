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

def frames_to_ms(fps: int) -> float:
    return 1000.0 / fps if fps > 0 else 0.0

class FrameBudget:
    def __init__(self, target_fps: int = 60):
        self.budget = frames_to_ms(target_fps)
        self.start = 0.0

    def __enter__(self):
        self.start = time.perf_counter() * 1000
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = (time.perf_counter() * 1000) - self.start
        if elapsed > self.budget:
            print(f'Frame budget exceeded by {elapsed - self.budget:.2f}ms')

def memoize_entity(func: Callable):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper