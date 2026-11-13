import time
import functools
from typing import Callable, Any

class PerformanceProfiler:
    def __init__(self):
        self.stats = {}

    def __call__(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = time.perf_counter() - start
            self.stats[func.__name__] = self.stats.get(func.__name__, []) + [duration]
            if duration > 0.016:
                print(f'[WARN] {func.__name__} dropped frames: {duration:.4f}s')
            return result
        return wrapper

    def report(self) -> None:
        for name, times in self.stats.items():
            avg = sum(times) / len(times)
            print(f'Function: {name} | Average latency: {avg:.6f}s')

frame_logger = PerformanceProfiler()

def log_performance(func: Callable) -> Callable:
    return frame_logger(func)

def get_telemetry_report() -> None:
    frame_logger.report()