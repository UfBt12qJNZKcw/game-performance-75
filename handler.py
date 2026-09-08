import time
import logging
from typing import Dict, Any

class PerformanceHandler:
    def __init__(self, threshold: float = 16.6):
        self.threshold = threshold
        self.metrics: Dict[str, list] = {'frame_times': []}
        self.logger = logging.getLogger('game-performance-75')

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = (time.perf_counter() - self.start) * 1000
        self.metrics['frame_times'].append(elapsed)
        if elapsed > self.threshold:
            self._trigger_spike_event(elapsed)

    def _trigger_spike_event(self, delta: float):
        self.logger.warning(f'frame spike detected: {delta:.2f}ms')

    def get_avg(self) -> float:
        data = self.metrics['frame_times']
        return sum(data) / len(data) if data else 0.0

def track_performance(func):
    def wrapper(*args, **kwargs):
        handler = PerformanceHandler()
        with handler:
            result = func(*args, **kwargs)
        return result
    return wrapper

if __name__ == '__main__':
    @track_performance
    def render_frame():
        time.sleep(0.01)

    render_frame()