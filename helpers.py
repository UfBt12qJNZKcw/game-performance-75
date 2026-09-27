import time
from functools import wraps
import gc

def throttle(interval):
    def decorator(func):
        last_called = [0.0]
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.perf_counter()
            if now - last_called[0] >= interval:
                last_called[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def memory_cleanup(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        gc.collect()
        return result
    return wrapper

def frame_budget(limit_ms):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = (time.perf_counter() - start) * 1000
            if elapsed > limit_ms:
                print(f"Warning: {func.__name__} exceeded budget: {elapsed:.2f}ms")
            return result
        return wrapper
    return decorator

def batch_process(data, chunk_size=100):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]