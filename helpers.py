import functools
import time
import logging

logger = logging.getLogger('performance-engine')

class PerformanceOptimizer:
    def __init__(self, threshold=0.016):
        self.threshold = threshold

    def profile_execution(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            if elapsed > self.threshold:
                logger.warning(f'framerate drop detected: {func.__name__} took {elapsed:.4f}s')
            return result
        return wrapper

def batch_process_objects(data, chunk_size=100):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def sanitize_frame_metrics(metrics: dict) -> dict:
    return {k: max(0.0, v) for k, v in metrics.items() if isinstance(v, (int, float))}

def frame_cooldown(seconds):
    def decorator(func):
        last_called = 0
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_called
            now = time.time()
            if now - last_called > seconds:
                last_called = now
                return func(*args, **kwargs)
            return None
        return wrapper
    return decorator