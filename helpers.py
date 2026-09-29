import time
import functools
import logging

def throttle(interval_ms):
    def decorator(func):
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.perf_counter() * 1000
            if now - last_called[0] >= interval_ms:
                last_called[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def frame_timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = (time.perf_counter() - start) * 1000
        if duration > 16.67:
            logging.warning(f'frame budget exceeded: {duration:.2f}ms in {func.__name__}')
        return result
    return wrapper

def memoize_buffer(capacity=128):
    def decorator(func):
        cache = {}
        def wrapper(*args):
            if args not in cache:
                if len(cache) >= capacity:
                    cache.pop(next(iter(cache)))
                cache[args] = func(*args)
            return cache[args]
        return wrapper
    return decorator

def lerp(a, b, t):
    return a + (b - a) * min(max(t, 0.0), 1.0)