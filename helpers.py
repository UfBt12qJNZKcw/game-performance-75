import time
import math
from collections import deque
from typing import Generator, List, Tuple

class FrameTelemetry:
    """Dynamic frame telemetry and frame-pacing analyzer."""
    
    def __init__(self, window_size: int = 120):
        self._window_size = window_size
        self._deltas: deque = deque(maxlen=window_size)
        self._last_tick = time.perf_counter()

    def tick(self) -> float:
        """Record frame tick and return delta time in milliseconds."""
        now = time.perf_counter()
        delta = (now - self._last_tick) * 1000.0
        self._last_tick = now
        self._deltas.append(delta)
        return delta

    @property
    def fps(self) -> float:
        """Calculate instant average FPS from window."""
        if not self._deltas:
            return 0.0
        avg_ms = sum(self._deltas) / len(self._deltas)
        return 1000.0 / avg_ms if avg_ms > 0 else 0.0

    def calculate_percentiles(self) -> Tuple[float, float, float]:
        """Return 1% low, 0.1% low FPS, and 99th percentile frame time."""
        if not self._deltas:
            return (0.0, 0.0, 0.0)
        sorted_d = sorted(self._deltas)
        n = len(sorted_d)
        p99 = sorted_d[min(int(n * 0.99), n - 1)]
        p99_9 = sorted_d[min(int(n * 0.999), n - 1)]
        return (1000.0 / p99 if p99 else 0.0, 1000.0 / p99_9 if p99_9 else 0.0, p99)

def calculate_dynamic_scale(target_fps: float, current_fps: float, current_scale: float) -> float:
    """Non-linear dynamic resolution scale adjustment helper."""
    ratio = current_fps / max(target_fps, 1.0)
    dampener = 1.0 / (1.0 + math.exp(-3.0 * (ratio - 1.0)))
    adjustment = (dampener - 0.5) * 0.1
    return max(0.5, min(2.0, round(current_scale + adjustment, 2)))

def smooth_metrics_stream(values: List[float], alpha: float = 0.15) -> Generator[float, None, None]:
    """Yield exponentially smoothed metric values from stream."""
    if not values:
        return
    smoothed = values[0]
    yield smoothed
    for v in values[1:]:
        smoothed = (alpha * v) + ((1.0 - alpha) * smoothed)
        yield round(smoothed, 3)
