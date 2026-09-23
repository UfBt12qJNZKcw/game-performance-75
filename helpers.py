import time
import functools
from typing import Callable, Any

def throttle_frame(ms: int = 16):
    """Artificially slows execution to mimic target frame times."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = (time.perf_counter() - start) * 1000
            sleep_time = (ms - elapsed) / 1000
            if sleep_time > 0:
                time.sleep(sleep_time)
            return result
        return wrapper
    return decorator

def memoize_resource(func: Callable):
    """Cache heavy asset lookups in a local dictionary."""
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

def lerp(start: float, end: float, alpha: float) -> float:
    """Linear interpolation for smooth camera or state transitions."""
    return start + (end - start) * max(0.0, min(1.0, alpha))

def clamp(value: float, min_val: float, max_val: float) -> float:
    """Constraint logic for game world coordinates."""
    return max(min_val, min(value, max_val))

def byte_size_formatter(size_bytes: int) -> str:
    """Human readable memory consumption stats."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f}{unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f}TB"