import time
import functools
from typing import Callable, Any

class PerformanceOptimizer:
    def __init__(self, target_fps: int = 60):
        self.frame_time = 1.0 / target_fps
        self.registry = {}

    def throttle(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_called = self.registry.get(func.__name__, 0)
            elapsed = time.perf_counter() - last_called
            if elapsed < self.frame_time:
                return None
            self.registry[func.__name__] = time.perf_counter()
            return func(*args, **kwargs)
        return wrapper

def resource_batch_cleanup(func: Callable) -> Callable:
    @functools.wraps(func)
    def cleaner(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        finally:
            import gc
            gc.collect()
    return cleaner

class FrameTracker:
    def __init__(self):
        self.start = time.perf_counter()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        delta = (time.perf_counter() - self.start) * 1000
        if delta > 16.6:
            print(f"Warning: Frame drop detected: {delta:.2f}ms")

def get_gpu_safe_identifier(name: str) -> str:
    return "".join([c for c in name if c.isalnum() or c in "_-"]).lower()