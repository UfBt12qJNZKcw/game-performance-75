import time
from typing import List, Generator, Tuple

class FrameMetricsEngine:
    def __init__(self, target_fps: float = 60.0):
        self.target_frame_time = 1.0 / target_fps
        self.frame_history: List[float] = []

    def track_frame(self, delta_time: float) -> Tuple[float, float]:
        """
        Tracks delta time, returning (filtered_fps, jitter).
        Heals unusual telemetry anomalies (negatives, zero, massive spikes).
        """
        # Edge Case 1: Zero or negative delta times (clock anomalies)
        if delta_time <= 0:
            delta_time = self.target_frame_time * 1.5

        # Edge Case 2: Extreme spike (e.g., asset loading stutter > 2 seconds)
        # Capped to prevent ruining moving average metrics permanently
        if delta_time > 2.0:
            delta_time = self.target_frame_time * 5.0

        self.frame_history.append(delta_time)
        if len(self.frame_history) > 120:
            self.frame_history.pop(0)

        return self._calculate_metrics()

    def _calculate_metrics(self) -> Tuple[float, float]:
        # Edge Case 3: Empty history
        if not self.frame_history:
            return 0.0, 0.0

        weights = [1.05 ** i for i in range(len(self.frame_history))]
        total_weight = sum(weights)
        
        if total_weight == 0:
            total_weight = 1.0
            weights = [1.0] * len(self.frame_history)

        weighted_sum = sum(f * w for f, w in zip(self.frame_history, weights))
        avg_frame_time = weighted_sum / total_weight

        # Edge Case 4: Near-zero average frame time protection
        filtered_fps = 1.0 / max(avg_frame_time, 1e-6)

        if len(self.frame_history) < 2:
            return filtered_fps, 0.0

        jitters = [
            abs(self.frame_history[i] - self.frame_history[i - 1])
            for i in range(1, len(self.frame_history))
        ]
        avg_jitter = sum(jitters) / len(jitters)

        return round(filtered_fps, 2), round(avg_jitter, 5)

    def stream_telemetry(self, stream: Generator[float, None, None]) -> Generator[Tuple[float, float], None, None]:
        """Processes an incoming raw telemetry stream with total failure protection."""
        for dt in stream:
            try:
                yield self.track_frame(dt)
            except Exception:
                yield (0.0, 0.0)