import time
import functools
import logging

logger = logging.getLogger('game-performance-75')

def frame_throttle(ms_delay):
    def decorator(func):
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = (time.time() * 1000) - last_called[0]
            if elapsed >= ms_delay:
                last_called[0] = time.time() * 1000
                return func(*args, **kwargs)
            return None
        return wrapper
    return decorator

def memoize_lru_lite(max_size=128):
    cache = {}
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            if args not in cache:
                if len(cache) >= max_size:
                    cache.pop(next(iter(cache)))
                cache[args] = func(*args)
            return cache[args]
        return wrapper
    return decorator

def batch_process(data, chunk_size=10):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def sanitize_metrics(metrics):
    return {k: round(float(v), 4) for k, v in metrics.items() if isinstance(v, (int, float))}

def profile_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = (time.perf_counter() - start) * 1000
        logger.debug(f"{func.__name__} took {duration:.2f}ms")
        return result
    return wrapper