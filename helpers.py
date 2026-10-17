import gc
import time
import psutil
import logging
from typing import Callable, Any

logger = logging.getLogger('game-performance-75')

class PerformanceOptimizer:
    def __init__(self, threshold_mb: float = 500.0):
        self.threshold = threshold_mb

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.trigger_reclamation()

    def trigger_reclamation(self):
        mem = psutil.Process().memory_info().rss / (1024 * 1024)
        if mem > self.threshold:
            logger.info(f'Memory usage at {mem:.2f}MB, forcing sweep')
            gc.collect()

class Throttle:
    def __init__(self, interval: float):
        self.interval = interval
        self.next_run = 0.0

    def __call__(self, func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            now = time.time()
            if now >= self.next_run:
                self.next_run = now + self.interval
                return func(*args, **kwargs)
        return wrapper

def batch_process(items: list, size: int):
    for i in range(0, len(items), size):
        yield items[i:i + size]

def memory_cleanup_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        gc.collect()
        return result
    return wrapper