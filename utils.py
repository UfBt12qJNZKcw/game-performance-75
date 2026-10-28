import gc
import time
import logging
from typing import Callable, Any

class PerformanceOptimizer:
    def __init__(self, threshold_ms: float = 16.6):
        self.threshold = threshold_ms
        self.logger = logging.getLogger('game-perf-75')

    def frame_monitor(self, func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = (time.perf_counter() - start) * 1000
            if duration > self.threshold:
                self.logger.warning(f'Frame spike detected: {duration:.2f}ms in {func.__name__}')
            return result
        return wrapper

    @staticmethod
    def purge_unreferenced_assets():
        gc.collect()
        return True

class ResourceRegistry:
    _store = {}

    @classmethod
    def register(cls, key: str, resource: Any):
        cls._store[key] = resource

    @classmethod
    def sweep(cls):
        cls._store.clear()
        gc.collect()