import time
import json
from datetime import datetime

class PerformanceMetrics:
    def __init__(self, log_file='game_metrics.jsonl'):
        self.log_file = log_file

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            duration = (time.perf_counter() - start_time) * 1000
            self._sink(func.__name__, duration)
            return result
        return wrapper

    def _sink(self, name, ms):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": name,
            "latency_ms": round(ms, 4),
            "status": "optimal" if ms < 16.67 else "stutter"
        }
        with open(self.log_file, 'a') as f:
            f.write(json.dumps(entry) + '\n')

def frame_logger(func):
    """decorator for tracking function execution timing"""
    logger = PerformanceMetrics()
    return logger(func)

if __name__ == '__main__':
    @frame_logger
    def render_frame(frame_id):
        time.sleep(0.01)
        return True

    render_frame(101)