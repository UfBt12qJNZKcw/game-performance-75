import logging
import functools
from typing import Callable, Any

logger = logging.getLogger('performance-75')

class PerformanceError(Exception):
    """Base exception for game engine anomalies."""
    pass

def robust_execution(retries: int = 3, fallback: Any = None):
    """Decorator for graceful degradation in frame processing."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_ex = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (MemoryError, RuntimeError) as e:
                    last_ex = e
                    logger.warning(f"Frame stutter: attempt {attempt+1} failed")
            
            if fallback is not None:
                return fallback
            raise PerformanceError(f"Critical core failure: {last_ex}") from last_ex
        return wrapper
    return decorator

def sanitize_frame_data(data: dict) -> dict:
    """Ensures frame packet integrity for render pipeline."""
    if not isinstance(data, dict):
        return {}
    return {k: v for k, v in data.items() if v is not None}

@robust_execution(retries=2, fallback={})
def safe_fetch(target: dict, key: str):
    """Safe access for volatile game state objects."""
    return target[key]