import time
from collections import deque
from contextlib import contextmanager
from typing import Dict, Generator

class GameFrameProfiler:
    """Monitors frame processing times and provides live performance analytics."""

    def __init__(self, window_size: int = 100):
        self.frame_durations: deque[float] = deque(maxlen=window_size)
        self.slow_frame_threshold_ms: float = 16.67

    @contextmanager
    def track(self) -> Generator[None, None, None]:
        start_time = time.perf_counter()
        try:
            yield
        finally:
            duration_ms = (time.perf_counter() - start_time) * 1000
            self.frame_durations.append(duration_ms)

    def get_telemetry(self) -> Dict[str, float]:
        if not self.frame_durations:
            return {"avg_fps": 0.0, "jitter_ms": 0.0, "slow_frames_pct": 0.0}

        total_frames = len(self.frame_durations)
        avg_duration_ms = sum(self.frame_durations) / total_frames
        avg_fps = 1000.0 / avg_duration_ms if avg_duration_ms > 0 else 0.0

        mean = avg_duration_ms
        variance = sum((x - mean) ** 2 for x in self.frame_durations) / total_frames
        jitter = variance ** 0.5

        slow_frames = sum(1 for x in self.frame_durations if x > self.slow_frame_threshold_ms)
        slow_frames_pct = (slow_frames / total_frames) * 100

        return {
            "avg_fps": round(avg_fps, 2),
            "jitter_ms": round(jitter, 3),
            "slow_frames_pct": round(slow_frames_pct, 2)
        }