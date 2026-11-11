import time
from collections import deque
from typing import Dict, List, Tuple

class FrameMetricsBuffer:
    """Sliding window circular buffer for high-precision frame timing statistics."""
    def __init__(self, capacity: int = 120):
        self.capacity = capacity
        self._frame_times_ns: deque = deque(maxlen=capacity)

    def record(self, duration_ns: int) -> None:
        self._frame_times_ns.append(duration_ns)

    @property
    def fps(self) -> float:
        if not self._frame_times_ns:
            return 0.0
        avg_ns = sum(self._frame_times_ns) / len(self._frame_times_ns)
        return 1_000_000_000.0 / avg_ns if avg_ns > 0 else 0.0

    def percentiles(self) -> Tuple[float, float, float]:
        """Returns (average, 1% low, 0.1% low) FPS metrics for smooth rendering assessment."""
        if not self._frame_times_ns:
            return (0.0, 0.0, 0.0)
        sorted_times = sorted(self._frame_times_ns)
        n = len(sorted_times)
        
        p99_idx = min(int(n * 0.99), n - 1)
        p999_idx = min(int(n * 0.999), n - 1)

        avg_fps = self.fps
        one_percent_low = 1_000_000_000.0 / sorted_times[p99_idx] if sorted_times[p99_idx] > 0 else 0.0
        point_one_low = 1_000_000_000.0 / sorted_times[p999_idx] if sorted_times[p999_idx] > 0 else 0.0

        return (round(avg_fps, 1), round(one_percent_low, 1), round(point_one_low, 1))

class FrameTicker:
    """Context manager and scope timer for measuring individual game ticks."""
    def __init__(self, buffer: FrameMetricsBuffer):
        self.buffer = buffer
        self._start_ns = 0

    def __enter__(self):
        self._start_ns = time.perf_counter_ns()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter_ns() - self._start_ns
        self.buffer.record(elapsed)

def analyze_frame_jitter(durations_ms: List[float]) -> Dict[str, float]:
    """Calculates variance and frame time jitter across recent frame samples."""
    if len(durations_ms) < 2:
        return {"jitter_ms": 0.0, "max_delta_ms": 0.0}
    
    deltas = [abs(durations_ms[i] - durations_ms[i - 1]) for i in range(1, len(durations_ms))]
    jitter = sum(deltas) / len(deltas)
    return {
        "jitter_ms": round(jitter, 3),
        "max_delta_ms": round(max(deltas), 3)
    }
