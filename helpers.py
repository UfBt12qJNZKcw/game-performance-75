import time
import functools
import logging

def time_execution(func):
    """Decorator for tracking frame-time bottlenecks in engine loop."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = (time.perf_counter() - start) * 1000
        if duration > 16.67:
            logging.warning(f"Frame drop: {func.__name__} took {duration:.2f}ms")
        return result
    return wrapper

def throttle(interval=0.1):
    """Prevents input spamming by rate-limiting calls."""
    def decorator(func):
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            if now - last_called[0] > interval:
                last_called[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def memoize_entity_lookup(func):
    """Cache-based lookup for static entity game data."""
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper