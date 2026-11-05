import time
import functools
from collections import deque

class FrameRateGovernor:
    """A jitter-resistant sliding window performance tracker."""
    def __init__(self, window_size=60):
        self.history = deque(maxlen=window_size)
        self.last_tick = time.perf_counter()

    def tick(self):
        now = time.perf_counter()
        delta = now - self.last_tick
        self.history.append(delta)
        self.last_tick = now

    @property
    def fps(self):
        if not self.history: return 0
        return 1.0 / (sum(self.history) / len(self.history))

def telemetry_throttle(interval=0.1):
    """Decorator to prevent high-frequency telemetry spam."""
    def decorator(func):
        last_called = 0
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_called
            now = time.time()
            if now - last_called > interval:
                last_called = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def normalize_vector(vec):
    """Vector normalization with safety epsilon for division."""
    magnitude = sum(x**2 for x in vec) ** 0.5
    if magnitude < 1e-9:
        return [0.0] * len(vec)
    return [x / magnitude for x in vec]