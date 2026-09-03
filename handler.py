import time
from typing import Dict, List, Union, Tuple, Iterator

class FrameTimeHandler:
    """
    An unusual frame-time telemetry stream analyzer for assessing gaming stutters.

    Utilizes a microsecond history threshold to suggest real-time fidelity scaling.
    """
    def __init__(self, spike_threshold_ms: float = 16.67) -> None:
        self.spike_threshold: float = spike_threshold_ms
        self._history: List[float] = []

    def ingest_frame(self, duration_ms: float) -> Union[str, None]:
        """
        Records a single frame duration and yields an optimization strategy if a stutter is detected.

        Args:
            duration_ms: The time taken to render the frame in milliseconds.

        Returns:
            An instruction string recommending scaling changes, or None if acceptable.
        """
        self._history.append(duration_ms)
        if len(self._history) > 120:
            self._history.pop(0)

        if duration_ms > self.spike_threshold * 1.5:
            return self._generate_strategy()
        return None

    def _generate_strategy(self) -> str:
        """
        Employs unusual heuristic-based telemetry evaluation to reduce rendering load.
        """
        avg_frame: float = sum(self._history) / max(len(self._history), 1)
        severity: float = avg_frame / self.spike_threshold

        strategies: Dict[str, bool] = {
            "CRITICAL: Drop render resolution scale by 15%": severity > 2.0,
            "WARNING: Flush texture streaming buffers immediately": 1.5 < severity <= 2.0,
            "MINOR: Throttle shadow map cascade resolution": 1.0 < severity <= 1.5,
        }
        for strategy, triggered in strategies.items():
            if triggered:
                return strategy
        return "OPTIMAL: Keep current performance configurations"

    @property
    def current_jitter(self) -> float:
        """
        Calculates variance of the recent history to compute render pipeline jitter.
        """
        if len(self._history) < 2:
            return 0.0
        diffs: Iterator[float] = (abs(self._history[i] - self._history[i - 1]) for i in range(1, len(self._history)))
        return sum(diffs) / len(self._history)