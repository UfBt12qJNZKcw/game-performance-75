from collections import deque
import time
from typing import Generator


class FrameTracker:
    """Creative moving-window frame timer using a high-precision generator ring."""

    def __init__(self, capacity: int = 120):
        self._samples: deque[int] = deque(maxlen=capacity)
        self._last_ns: int = time.perf_counter_ns()

    def tick(self) -> float:
        """Record frame end, returns frame duration in milliseconds."""
        now = time.perf_counter_ns()
        delta_ms = (now - self._last_ns) / 1_000_000.0
        self._last_ns = now
        self._samples.append(now)
        return delta_ms

    @property
    def fps(self) -> float:
        """Calculate current FPS from time differential across sample window."""
        if len(self._samples) < 2:
            return 0.0
        elapsed_sec = (self._samples[-1] - self._samples[0]) / 1_000_000_000.0
        return (len(self._samples) - 1) / elapsed_sec if elapsed_sec > 0 else 0.0


def calculate_stutter_index(frame_times_ms: list[float], target_ms: float = 16.67) -> float:
    """Measures deviation intensity from target frame budget using exponential scaling."""
    if not frame_times_ms:
        return 0.0
    spikes = [max(0.0, ft - target_ms) ** 1.5 for ft in frame_times_ms]
    return round(sum(spikes) / len(frame_times_ms), 3)


def parse_hardware_flags(mask: int, features: list[str]) -> dict[str, bool]:
    """Unpacks bitwise graphic feature toggles into explicit boolean flags map."""
    return {feature: bool(mask & (1 << idx)) for idx, feature in enumerate(features)}


def frame_rate_limiter(fps_cap: int) -> Generator[None, None, None]:
    """Generator-based frame pacing delay yield loop."""
    target_interval = 1.0 / max(1, fps_cap)
    last_frame = time.perf_counter()
    while True:
        elapsed = time.perf_counter() - last_frame
        sleep_time = target_interval - elapsed
        if sleep_time > 0:
            time.sleep(sleep_time)
        last_frame = time.perf_counter()
        yield
