import gc
import time
import psutil
from typing import Callable, Any

class MemorySentinel:
    def __init__(self, threshold_mb: int = 500):
        self.threshold = threshold_mb
        self.process = psutil.Process()

    def is_overloaded(self) -> bool:
        return (self.process.memory_info().rss / 1024 / 1024) > self.threshold

    def emergency_cleanup(self):
        gc.collect()
        time.sleep(0.01)

def performance_guard(func: Callable) -> Callable:
    sentinel = MemorySentinel()
    def wrapper(*args, **kwargs) -> Any:
        if sentinel.is_overloaded():
            sentinel.emergency_cleanup()
        return func(*args, **kwargs)
    return wrapper

def throttle_frame_rate(target_fps: int):
    frame_time = 1.0 / target_fps
    last_time = time.perf_counter()

    def decorator(func: Callable) -> Callable:
        def throttled(*args, **kwargs):
            nonlocal last_time
            current_time = time.perf_counter()
            elapsed = current_time - last_time
            if elapsed < frame_time:
                time.sleep(frame_time - elapsed)
            last_time = time.perf_counter()
            return func(*args, **kwargs)
        return throttled
    return decorator