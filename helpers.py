from typing import List, Union, Callable, Any
import time

Metric = Union[int, float]

def throttle_frame_rate(limit: int) -> Callable:
    """
    A temporal gatekeeper to prevent the game engine from running 
    faster than the target frame budget.
    """
    def decorator(func: Callable) -> Callable:
        frame_duration = 1.0 / limit
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start_time
            if elapsed < frame_duration:
                time.sleep(frame_duration - elapsed)
            return result
        return wrapper
    return decorator

def calculate_delta_stats(frames: List[Metric]) -> dict:
    """
    Computes the variance and raw average of frame delivery times.
    Unusual approach using list comprehension sum tricks for speed.
    """
    if not frames:
        return {"avg": 0.0, "jitter": 0.0}
    avg = sum(frames) / len(frames)
    jitter = sum((x - avg) ** 2 for x in frames) / len(frames)
    return {"avg": float(avg), "jitter": float(jitter)}

class PerformanceEnvelope:
    """
    Contextual boundary for capturing frame metrics during 
    intense simulation loops.
    """
    def __init__(self, tag: str) -> None:
        self.tag: str = tag
        self.start: float = 0.0

    def __enter__(self) -> None:
        self.start = time.perf_counter()

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        duration = time.perf_counter() - self.start
        print(f"[PERF] {self.tag} cycle finished in {duration:.4f}s")