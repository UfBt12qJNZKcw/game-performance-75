import gc
import time
import psutil
from typing import Callable, Any

class MemoryManager:
    def __init__(self, threshold_mb: float = 512.0):
        self.threshold = threshold_mb

    def __call__(self, func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            self._auto_purge()
            return result
        return wrapper

    def _auto_purge(self):
        process = psutil.Process()
        mem_info = process.memory_info().rss / (1024 * 1024)
        if mem_info > self.threshold:
            gc.collect()

class FrameThrottle:
    def __init__(self, fps: int = 60):
        self.interval = 1.0 / fps
        self.last_frame = time.perf_counter()

    def wait(self):
        elapsed = time.perf_counter() - self.last_frame
        if elapsed < self.interval:
            time.sleep(self.interval - elapsed)
        self.last_frame = time.perf_counter()

def sanitize_metrics(data: dict) -> dict:
    return {str(k): float(v) for k, v in data.items() if isinstance(v, (int, float))}

class PerformanceRegistry:
    _storage = {}

    @classmethod
    def track(cls, key: str, value: Any):
        cls._storage[key] = value

    @classmethod
    def dump(cls):
        return dict(cls._storage)