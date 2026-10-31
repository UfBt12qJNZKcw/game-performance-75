"""Frame time monitoring and performance telemetry processing engine."""

import math
from typing import List, Dict, Final, TypeAlias, Union

FrameDeltaMs: TypeAlias = float
PercentileLow: TypeAlias = float


class FrameTimeProcessor:
    """Processes raw frame intervals using custom percentile estimation.
    
    Evaluates real-time gaming frame rendering metrics, detecting micro-stutters
    and calculating 1% and 0.1% frame time lows without external dependencies.
    """

    __slots__ = ("_buffer", "_capacity", "_alpha")

    def __init__(self, history_size: int = 120, smoothing: float = 0.15) -> None:
        self._buffer: List[FrameDeltaMs] = []
        self._capacity: Final[int] = history_size
        self._alpha: Final[float] = smoothing

    def ingest(self, delta_time_ms: FrameDeltaMs) -> "FrameTimeProcessor":
        """Ingest a new frame rendering time into the sliding ring buffer.
        
        Args:
            delta_time_ms: Frame rendering duration in milliseconds.
            
        Returns:
            Self instance to allow fluid method chaining.
        """
        if len(self._buffer) >= self._capacity:
            self._buffer.pop(0)
        self._buffer.append(max(0.001, float(delta_time_ms)))
        return self

    def __getitem__(self, percentile: float) -> PercentileLow:
        """Retrieve arbitrary frame time percentile via subscript indexing.
        
        Usage: processor[0.99] returns the 99th percentile frame time.
        """
        if not self._buffer:
            return 0.0
        sorted_frames: List[float] = sorted(self._buffer)
        idx: int = min(
            len(sorted_frames) - 1,
            max(0, math.ceil(percentile * len(sorted_frames)) - 1)
        )
        return sorted_frames[idx]

    def calculate_telemetry(self) -> Dict[str, Union[float, int]]:
        """Generates composite performance metrics for HUD overlay.
        
        Returns:
            Dictionary containing average FPS, 1% low FPS, 0.1% low FPS, and stutter count.
        """
        if not self._buffer:
            return {"avg_fps": 0.0, "low_1pct": 0.0, "low_01pct": 0.0, "stutters": 0}

        avg_ms: float = sum(self._buffer) / len(self._buffer)
        one_pct_ms: float = self[0.99]
        tenth_pct_ms: float = self[0.999]
        
        stutter_count: int = sum(1 for dt in self._buffer if dt > (avg_ms * 2.5))

        return {
            "avg_fps": round(1000.0 / avg_ms, 1),
            "low_1pct": round(1000.0 / one_pct_ms, 1),
            "low_01pct": round(1000.0 / tenth_pct_ms, 1),
            "stutters": stutter_count,
        }
