import time
import functools
import psutil
import gc

def throttled_frame_update(threshold_ms):
    def decorator(func):
        last_call = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.perf_counter() * 1000
            if now - last_call[0] >= threshold_ms:
                last_call[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def memory_pressure_cleanup(limit_mb=512):
    process = psutil.Process()
    if process.memory_info().rss / (1024 * 1024) > limit_mb:
        gc.collect()
        return True
    return False

def dynamic_buffer_scaler(base_size, framerate):
    """Calculates object pooling size based on current performance."""
    target_fps = 144
    multiplier = max(0.5, min(2.0, target_fps / framerate))
    return int(base_size * multiplier)

class PerformanceSnapshot:
    def __init__(self):
        self.start = time.perf_counter()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = (time.perf_counter() - self.start) * 1000
        if elapsed > 16.6:
            print(f"Warning: Frame budget exceeded: {elapsed:.2f}ms")