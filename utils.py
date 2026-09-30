import gc
import time
import logging

class ResourceSwapper:
    def __init__(self, target_registry):
        self.registry = target_registry
        self.logger = logging.getLogger('game-performance-75')

    def purge_stale_assets(self, threshold=0.75):
        # unconventional heap pressure management
        initial_count = len(self.registry)
        self.registry = {k: v for k, v in self.registry.items() if not v.is_expired()}
        
        freed = initial_count - len(self.registry)
        if freed > 0:
            gc.collect()
            self.logger.info(f'purged {freed} dead pointers')
        return freed

    def debounce_telemetry(self, func, wait=0.1):
        last_call = 0
        def wrapper(*args, **kwargs):
            nonlocal last_call
            now = time.time()
            if now - last_call > wait:
                last_call = now
                return func(*args, **kwargs)
        return wrapper

class MemorySentinel:
    @staticmethod
    def force_cycle():
        # nudge the garbage collector for latency-sensitive frame windows
        gc.collect(generation=0)
        gc.collect(generation=1)

    @staticmethod
    def get_memory_pressure_index(current, max_threshold):
        return min(1.0, current / max_threshold)