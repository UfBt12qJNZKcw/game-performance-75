import time
import functools
from typing import Callable, Any

def throttle_frame_rate(fps: int):
    def decorator(func: Callable):
        interval = 1.0 / fps
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.perf_counter() - last_called[0]
            if elapsed >= interval:
                last_called[0] = time.perf_counter()
                return func(*args, **kwargs)
            return None
        return wrapper
    return decorator

def memoize_entity_data(func: Callable):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

class PerformanceOptimizer:
    @staticmethod
    def clamp(value: float, min_val: float, max_val: float) -> float:
        return max(min_val, min(value, max_val))

    @staticmethod
    def serialize_vector(vec: tuple) -> str:
        return ':'.join(map(str, vec))

    @staticmethod
    def batch_process(data: list, func: Callable, chunk_size: int = 10):
        for i in range(0, len(data), chunk_size):
            yield [func(item) for item in data[i:i + chunk_size]]

def debug_log_execution(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f'[PERF] {func.__name__} took {time.perf_counter() - start:.6f}s')
        return result
    return wrapper