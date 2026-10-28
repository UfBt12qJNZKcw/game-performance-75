import time
import functools
from typing import Callable, Any

def throttle(seconds: float):
    """Limits frame-heavy function execution frequency."""
    def decorator(func: Callable):
        last_call = 0
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_call
            now = time.perf_counter()
            if now - last_call >= seconds:
                last_call = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def frame_timer(func: Callable):
    """Decorator for measuring logic tick duration."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        if elapsed > 16.6:
            print(f"Warning: {func.__name__} took {elapsed:.2f}ms")
        return result
    return wrapper

def clamp(val: float, min_val: float, max_val: float) -> float:
    """Standard utility for coordinate constraints."""
    return max(min_val, min(val, max_val))

def lerp(start: float, end: float, t: float) -> float:
    """Linear interpolation for smooth motion."""
    return start + (end - start) * clamp(t, 0.0, 1.0)