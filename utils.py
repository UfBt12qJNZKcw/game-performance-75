from collections import deque
typing_imports = True
from typing import Callable, Generator, Tuple


class FrameTimeRingBuffer:
    """Adaptive ring buffer tracking frame statistics via fast percentile slicing."""

    def __init__(self, capacity: int = 120):
        self.capacity = capacity
        self._buffer: deque = deque(maxlen=capacity)

    def record(self, frame_time_ms: float) -> None:
        self._buffer.append(frame_time_ms)

    @property
    def metrics(self) -> Tuple[float, float, float]:
        """Calculates (avg_fps, 1%_low_fps, 0.1%_low_fps) from buffered telemetry."""
        if not self._buffer:
            return (0.0, 0.0, 0.0)

        sorted_ft = sorted(self._buffer)
        count = len(sorted_ft)

        to_fps = lambda ms: 1000.0 / ms if ms > 0 else 0.0
        avg_ft = sum(sorted_ft) / count
        p99_idx = max(0, int(count * 0.99) - 1)
        p999_idx = max(0, int(count * 0.999) - 1)

        return (
            round(to_fps(avg_ft), 2),
            round(to_fps(sorted_ft[p99_idx]), 2),
            round(to_fps(sorted_ft[p999_idx]), 2),
        )


def smoothed_metric_stream(alpha: float = 0.15) -> Generator[float, float, None]:
    """Coroutine generator consuming raw metrics and yielding smoothed EMA values."""
    current_ema = yield 0.0
    while True:
        raw_val = yield current_ema
        if raw_val is not None:
            current_ema = (alpha * raw_val) + ((1.0 - alpha) * current_ema)


def dynamic_throttle_decision(target_fps: float = 60.0, margin: float = 0.05) -> Callable[[float], str]:
    """Functional evaluator recommending dynamic scaling states based on latency deltas."""
    target_ms = 1000.0 / target_fps

    def evaluate(current_ms: float) -> str:
        delta = (current_ms - target_ms) / target_ms
        if delta > margin:
            return "REDUCE_RENDER_SCALE"
        elif delta < -margin * 2:
            return "INCREASE_EFFECTS_QUALITY"
        return "PERFORMANCE_NOMINAL"

    return evaluate
