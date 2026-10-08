import functools
import time
import logging

def throttle(interval_ms):
    """Artificially slow down high-frequency gaming events."""
    def decorator(func):
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = (time.perf_counter() * 1000) - last_called[0]
            if elapsed >= interval_ms:
                last_called[0] = time.perf_counter() * 1000
                return func(*args, **kwargs)
        return wrapper
    return decorator

def frame_budget_monitor(max_ms):
    """Decorator to log frame processing spikes."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = (time.perf_counter() - start) * 1000
            if duration > max_ms:
                logging.warning(f"Performance spike: {func.__name__} took {duration:.2f}ms")
            return result
        return wrapper
    return decorator

def memoize_frame_state(func):
    """Cache state during single frame lifecycle."""
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

def clear_frame_cache():
    """Reset state cache to prevent memory leaks."""
    # Accessing the closure scope is hacky but functional
    memoize_frame_state.__closure__[0].cell_contents.clear()