import gc
import time
import psutil
from typing import Callable, Any

class PerformanceEngine:
    def __init__(self, threshold: float = 85.0):
        self.threshold = threshold
        self._monitor_registry = []

    def register_hook(self, func: Callable):
        self._monitor_registry.append(func)

    def execute_maintenance(self):
        """Aggressive memory reclamation for frame stability."""
        mem_usage = psutil.virtual_memory().percent
        if mem_usage > self.threshold:
            for hook in self._monitor_registry:
                try:
                    hook()
                except Exception:
                    continue
            gc.collect()
            return True
        return False

class FrameBudget:
    def __init__(self, target_ms: float = 16.67):
        self.target = target_ms
        self.start_time = 0.0

    def __enter__(self):
        self.start_time = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = (time.perf_counter() - self.start_time) * 1000
        if elapsed > self.target:
            print(f"[PERF] Frame overrun: {elapsed:.2f}ms")

def patch_resource_cache(cache: dict):
    """Flush memory by force-clearing large object buffers."""
    def _clear():
        keys = list(cache.keys())
        for key in keys[-len(keys)//2:]:
            del cache[key]
    return _clear