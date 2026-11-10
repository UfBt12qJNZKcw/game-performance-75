from collections import deque
from functools import reduce
import heapq
from typing import Callable, Dict, List, Tuple


class FrameMetricsProcessor:
    """Dynamic pipeline processor for gaming frame time analysis."""

    def __init__(self, target_fps: int = 60, window_size: int = 120):
        self.target_delta = 1000.0 / target_fps
        self.history: deque[float] = deque(maxlen=window_size)
        self._transformers: List[Callable[[float], float]] = []

    def pipe(self, transformer: Callable[[float], float]) -> "FrameMetricsProcessor":
        """Chain transform functions dynamically into frame processing."""
        self._transformers.append(transformer)
        return self

    def ingest(self, frame_time_ms: float) -> float:
        """Process frame time through chained transformations and log history."""
        processed = reduce(lambda val, fn: fn(val), self._transformers, frame_time_ms)
        self.history.append(processed)
        return processed

    def calculate_percentiles(self, percentiles: Tuple[float, ...] = (95.0, 99.0)) -> Dict[str, float]:
        """Compute p95/p99 frame times using heap sort technique."""
        if not self.history:
            return {f"p{int(p)}": 0.0 for p in percentiles}
        sorted_samples = heapq.nsmallest(len(self.history), self.history)
        n = len(sorted_samples)
        return {
            f"p{int(p)}": sorted_samples[min(int((p / 100.0) * n), n - 1)]
            for p in percentiles
        }

    def stutter_ratio(self) -> float:
        """Calculate ratio of frames exceeding 1.5x target frame time."""
        if not self.history:
            return 0.0
        stutters = sum(1 for dt in self.history if dt > self.target_delta * 1.5)
        return round(stutters / len(self.history), 4)


def clamp_frame_delta(max_delta_ms: float = 100.0) -> Callable[[float], float]:
    """Helper closure preventing runaway delta spikes during lag spikes."""
    return lambda dt: min(max(dt, 0.1), max_delta_ms)


def ewma_smoothing(alpha: float = 0.2) -> Callable[[float], float]:
    """Stateful closure maintaining exponential weighted moving average."""
    state: Dict[str, float | None] = {"avg": None}

    def _smooth(dt: float) -> float:
        current = state["avg"]
        state["avg"] = dt if current is None else (alpha * dt + (1 - alpha) * current)
        return state["avg"]

    return _smooth