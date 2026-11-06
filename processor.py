from collections import deque
from dataclasses import dataclass
import math
from typing import Generator, Iterable, NamedTuple


class FrameMetrics(NamedTuple):
    avg_fps: float
    one_percent_low: float
    zero_one_percent_low: float
    stutter_count: int


@dataclass(slots=True)
class StreamConfig:
    window_size: int = 1000
    stutter_threshold_ms: float = 16.67


def process_frametime_stream(
    frametimes_ms: Iterable[float], config: StreamConfig = StreamConfig()
) -> Generator[FrameMetrics, None, None]:
    """Processes continuous stream of frame times using rolling percentile estimation."""
    window: deque[float] = deque(maxlen=config.window_size)
    stutter_tracker = 0

    for ft in frametimes_ms:
        if ft <= 0:
            continue

        window.append(ft)
        stutter_tracker = (
            stutter_tracker + 1
            if ft > config.stutter_threshold_ms * 1.5
            else max(0, stutter_tracker - 1)
        )

        if len(window) < 10:
            continue

        sorted_win = sorted(window)
        n = len(sorted_win)

        idx_1pct = max(0, math.floor(n * 0.01))
        idx_01pct = max(0, math.floor(n * 0.001))

        avg_ft = sum(window) / n
        avg_fps = 1000.0 / avg_ft if avg_ft > 0 else 0.0

        worst_ft_1pct = sorted_win[-1 - idx_1pct]
        worst_ft_01pct = sorted_win[-1 - idx_01pct]

        one_low = 1000.0 / worst_ft_1pct if worst_ft_1pct > 0 else 0.0
        zero_one_low = 1000.0 / worst_ft_01pct if worst_ft_01pct > 0 else 0.0

        yield FrameMetrics(
            avg_fps=round(avg_fps, 2),
            one_percent_low=round(one_low, 2),
            zero_one_percent_low=round(zero_one_low, 2),
            stutter_count=stutter_tracker,
        )


def calculate_frame_pacing_score(frametimes: list[float]) -> float:
    """Calculates frame pacing uniformity score using jitter variance scaling."""
    if len(frametimes) < 2:
        return 100.0
    deltas = [abs(frametimes[i] - frametimes[i - 1]) for i in range(1, len(frametimes))]
    mean_delta = sum(deltas) / len(deltas)
    jitter = math.sqrt(sum((d - mean_delta) ** 2 for d in deltas) / len(deltas))
    return max(0.0, round(100.0 - (jitter * 2.5), 2))
