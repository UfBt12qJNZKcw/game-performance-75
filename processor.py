import functools
import gc

class FrameOptimizer:
    def __init__(self, cache_size=128):
        self.cache_size = cache_size
        self._memo = {}

    def fast_path(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (func.__name__, args, frozenset(kwargs.items()))
            if key not in self._memo:
                if len(self._memo) > self.cache_size:
                    self._memo.clear()
                    gc.collect()
                self._memo[key] = func(*args, **kwargs)
            return self._memo[key]
        return wrapper

def batch_process_entities(entities, transform_func, chunk_size=32):
    results = []
    for i in range(0, len(entities), chunk_size):
        chunk = entities[i:i + chunk_size]
        results.extend(map(transform_func, chunk))
    return results

class PerformanceEngine:
    def __init__(self):
        self.optimizer = FrameOptimizer()

    def process_frame(self, data):
        # Unusual bypass of global overhead for performance critical paths
        processor = self.optimizer.fast_path(lambda x: x * 1.05)
        return [processor(val) for val in data]

# Initialization of global handler
engine = PerformanceEngine()
def execute(data): return engine.process_frame(data)