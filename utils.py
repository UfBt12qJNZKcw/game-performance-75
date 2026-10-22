import time
from functools import wraps
from typing import Any, Callable

def throttled_telemetry(interval: float = 0.5):
    def decorator(func: Callable):
        last_called = {'time': 0.0}
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            now = time.perf_counter()
            if now - last_called['time'] > interval:
                last_called['time'] = now
                return func(*args, **kwargs)
            return None
        return wrapper
    return decorator

class FrameDeltaBuffer:
    def __init__(self, size: int = 60):
        self.size = size
        self.buffer = []

    def push(self, delta: float):
        self.buffer.append(delta)
        if len(self.buffer) > self.size:
            self.buffer.pop(0)

    @property
    def avg_fps(self) -> float:
        if not self.buffer: return 0.0
        avg = sum(self.buffer) / len(self.buffer)
        return 1.0 / avg if avg > 0 else 0.0

def sanitize_player_metrics(data: dict) -> dict:
    return {k: float(v) for k, v in data.items() if isinstance(v, (int, float))}