import bisect
import collections
import math
from typing import List, Tuple


class FrameTimeTracker:
    """A rolling buffer tracker for game frame times in milliseconds with dynamic percentiles."""

    def __init__(self, max_samples: int = 1000):
        self.max_samples = max_samples
        self.history = collections.deque(maxlen=max_samples)
        self.sorted_history: List[float] = []

    def record_frame(self, frame_time_ms: float) -> None:
        if len(self.history) == self.max_samples:
            oldest = self.history[0]
            idx = bisect.bisect_left(self.sorted_history, oldest)
            if idx < len(self.sorted_history) and self.sorted_history[idx] == oldest:
                self.sorted_history.pop(idx)

        self.history.append(frame_time_ms)
        bisect.insort(self.sorted_history, frame_time_ms)

    def get_metrics(self) -> Tuple[float, float, float]:
        """Returns (average_fps, one_percent_low_fps, zero_point_one_percent_low_fps)."""
        if not self.sorted_history:
            return 0.0, 0.0, 0.0

        total_time = sum(self.sorted_history)
        avg_frame_time = total_time / len(self.sorted_history)
        avg_fps = 1000.0 / avg_frame_time if avg_frame_time > 0 else 0.0

        size = len(self.sorted_history)
        one_percent_idx = max(0, size - max(1, math.ceil(size * 0.01)))
        zero_one_percent_idx = max(0, size - max(1, math.ceil(size * 0.001)))

        one_percent_low_ms = self.sorted_history[one_percent_idx]
        zero_one_percent_low_ms = self.sorted_history[zero_one_percent_idx]

        one_percent_fps = 1000.0 / one_percent_low_ms if one_percent_low_ms > 0 else 0.0
        zero_one_percent_fps = 1000.0 / zero_one_percent_low_ms if zero_one_percent_low_ms > 0 else 0.0

        return avg_fps, one_percent_fps, zero_one_percent_fps

    def clear_spikes(self, threshold_ms: float) -> int:
        """Removes abnormal frame spikes above a given threshold to clean performance datasets."""
        removed_count = 0
        new_history = collections.deque(maxlen=self.max_samples)
        self.sorted_history.clear()

        for ft in self.history:
            if ft <= threshold_ms:
                new_history.append(ft)
                bisect.insort(self.sorted_history, ft)
            else:
                removed_count += 1

        self.history = new_history
        return removed_count
