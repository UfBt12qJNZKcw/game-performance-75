import time
import functools
import logging

logger = logging.getLogger('game-performance-75')

class PerformanceProfiler:
    """Decorator class to monitor frame-sensitive operations."""
    def __init__(self, threshold_ms=16.67):
        self.threshold = threshold_ms

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = (time.perf_counter() - start) * 1000
            if duration > self.threshold:
                logger.warning(f"Slow frame in {func.__name__}: {duration:.2f}ms")
            return result
        return wrapper

def memory_efficient_cleanup(obj_refs: list):
    """Aggressive memory reclamation for dormant game assets."""
    import gc
    for ref in obj_refs:
        if hasattr(ref, 'unload'):
            ref.unload()
    gc.collect()

class ResourceRegistry:
    """Registry for managing active game entities."""
    _pool = {}

    @classmethod
    def register(cls, key, instance):
        cls._pool[key] = instance

    @classmethod
    def purge(cls):
        cls._pool.clear()

def get_frame_budget(fps_target: int = 60) -> float:
    """Calculation of frame budget per target fps."""
    return 1000.0 / fps_target