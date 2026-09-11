import time
from typing import Callable, Any, Dict, TypeVar

T = TypeVar('T')

def performance_throttle(interval: float) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Decorator to ensure function execution does not exceed frequency."""
    last_called: Dict[str, float] = {'ts': 0.0}

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        def wrapper(*args: Any, **kwargs: Any) -> T:
            now: float = time.perf_counter()
            elapsed: float = now - last_called['ts']
            if elapsed < interval:
                time.sleep(interval - elapsed)
            last_called['ts'] = time.perf_counter()
            return func(*args, **kwargs)
        return wrapper
    return decorator

def frame_delta_scaler(base_fps: float = 60.0) -> Callable[[float], float]:
    """Factory for frame-independent movement coefficient calculation."""
    def scaler(current_delta: float) -> float:
        return current_delta * base_fps
    return scaler

def memory_pressure_check(limit_mb: float = 1024.0) -> bool:
    """Quick health check against game memory heap footprint."""
    import os
    import psutil
    process = psutil.Process(os.getpid())
    usage_mb: float = process.memory_info().rss / (1024 * 1024)
    return usage_mb < limit_mb