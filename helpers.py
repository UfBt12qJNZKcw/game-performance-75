import time
import math
from typing import Callable, Any, Tuple
from functools import wraps

def fps_budget(target_fps: float = 60.0, strict: bool = False):
    """Decorator tracking function runtime against target frame budget."""
    target_dt = 1.0 / target_fps
    
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Tuple[Any, float, bool]:
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            overbudget = elapsed > target_dt
            if overbudget and strict:
                time.sleep(max(0.0, target_dt - elapsed))
            return result, elapsed, overbudget
        return wrapper
    return decorator

def quantize_frame_delta(delta_time: float, monitor_hz: int = 144) -> float:
    """Snaps frame delta times to discrete monitor refresh v-sync ticks."""
    if delta_time <= 0:
        return 0.0
    vsync_interval = 1.0 / monitor_hz
    intervals = round(delta_time / vsync_interval)
    return max(vsync_interval, intervals * vsync_interval)

class FrameTimeHistogram:
    """Fixed-bucket array for sub-millisecond stutter analysis."""
    def __init__(self, max_ms: int = 100):
        self.max_ms = max_ms
        self.buckets = [0] * (max_ms + 1)
        self.total_frames = 0

    def record(self, dt_seconds: float) -> None:
        ms = min(self.max_ms, int(dt_seconds * 1000.0))
        self.buckets[ms] += 1
        self.total_frames += 1

    def percentile(self, p: float) -> float:
        if self.total_frames == 0:
            return 0.0
        target = math.ceil((p / 100.0) * self.total_frames)
        accum = 0
        for ms, count in enumerate(self.buckets):
            accum += count
            if accum >= target:
                return ms / 1000.0
        return self.max_ms / 1000.0
