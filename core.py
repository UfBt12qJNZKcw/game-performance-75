import gc
import time
import functools

def frame_optimizer(target_fps=60):
    frame_time = 1.0 / target_fps
    def decorator(func):
        last_call = 0.0
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_call
            now = time.perf_counter()
            elapsed = now - last_call
            if elapsed < frame_time:
                time.sleep(frame_time - elapsed)
            result = func(*args, **kwargs)
            last_call = time.perf_counter()
            return result
        return wrapper
    return decorator

class MemoryThrottle:
    def __init__(self, threshold_mb=500):
        self.threshold = threshold_mb

    def monitor_and_clean(self):
        import os, psutil
        process = psutil.Process(os.getpid())
        mem_usage = process.memory_info().rss / (1024 * 1024)
        if mem_usage > self.threshold:
            gc.collect()

class GameCore:
    def __init__(self):
        self.throttle = MemoryThrottle()

    @frame_optimizer(target_fps=144)
    def process_tick(self, entity_data):
        self.throttle.monitor_and_clean()
        return [e * 1.05 for e in entity_data]