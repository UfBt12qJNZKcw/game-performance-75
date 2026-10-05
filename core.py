import gc
import time
import psutil
from typing import Callable

class PerformanceOptimizer:
    def __init__(self, threshold_mb: float = 500.0):
        self.threshold = threshold_mb
        self.registry: list[Callable] = []

    def register_cleanup(self, func: Callable):
        self.registry.append(func)

    def pulse(self):
        mem = psutil.Process().memory_info().rss / (1024 * 1024)
        if mem > self.threshold:
            [task() for task in self.registry]
            gc.collect()

    def run_cycle(self, tasks: list[Callable]):
        start = time.perf_counter()
        try:
            [t() for t in tasks]
        finally:
            self.pulse()
        return time.perf_counter() - start

class ResourceManager:
    def __init__(self):
        self.assets = {}

    def purge_stale(self):
        keys = list(self.assets.keys())
        for k in keys:
            if self.assets[k].expired:
                del self.assets[k]

class GameEngine:
    def __init__(self):
        self.optimizer = PerformanceOptimizer()
        self.manager = ResourceManager()
        self.optimizer.register_cleanup(self.manager.purge_stale)

    def tick(self, frame_logic: Callable):
        return self.optimizer.run_cycle([frame_logic])