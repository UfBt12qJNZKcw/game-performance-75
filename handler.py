import math
from collections import deque
from typing import Generator, List, Tuple

class JitterBuffer:
    """
    An unusual frame-time telemetry handler that uses a Fibonacci-weighted
    sliding window to filter out anomalous spikes (like loading screens)
    and highlight micro-stutters.
    """
    def __init__(self, capacity: int = 8) -> None:
        self.capacity = max(3, capacity)
        self.buffer: deque = deque(maxlen=self.capacity)
        self.weights = self._generate_fib_weights(self.capacity)

    def _generate_fib_weights(self, n: int) -> List[float]:
        weights = [1.0, 1.0]
        for _ in range(n - 2):
            weights.append(weights[-1] + weights[-2])
        total = sum(weights)
        return [w / total for w in weights]

    def process_frame(self, frame_time_ms: float) -> Tuple[float, str]:
        if frame_time_ms > 500.0:
            return 0.0, "EXCLUDE_LOADING_OR_PAUSE"

        self.buffer.append(frame_time_ms)
        if len(self.buffer) < self.capacity:
            return 0.0, "BUFFERING"

        weighted_mean = sum(f * w for f, w in zip(self.buffer, self.weights))
        variance = sum(w * ((f - weighted_mean) ** 2) for f, w in zip(self.buffer, self.weights))
        jitter = math.sqrt(variance)

        ratio = jitter / (weighted_mean + 1e-9)
        if ratio > 0.3:
            status = "CRITICAL_STUTTER"
        elif ratio > 0.15:
            status = "MICRO_STUTTER"
        else:
            status = "FLUID"

        return round(jitter, 3), status

def stream_telemetry(raw_stream: List[float]) -> Generator[Tuple[float, str], None, None]:
    handler = JitterBuffer()
    for frame in raw_stream:
        yield handler.process_frame(frame)
