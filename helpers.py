import time
import functools
from typing import Callable, Any

def throttle(seconds: float):
    """Limits execution frequency of expensive gaming logic."""
    def decorator(func: Callable):
        last_call = 0
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_call
            now = time.perf_counter()
            if now - last_call > seconds:
                last_call = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def clamp(value: float, min_val: float, max_val: float) -> float:
    """Constrains movement or value metrics to valid bounds."""
    return max(min_val, min(value, max_val))

def memoize_frame(func: Callable):
    """Short-lived cache for per-frame physics calculations."""
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

def time_execution(func: Callable):
    """Performance monitoring for heavy rendering loops."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        if duration > 0.016:  # 60fps threshold
            print(f"Warning: {func.__name__} took {duration:.4f}s")
        return result
    return wrapper