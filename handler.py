import functools
import logging
from typing import Callable, Any

logger = logging.getLogger('game-performance-75')

class PerformanceConstraintError(Exception):
    """Raised when game loop exceeds frame budget."""
    pass

def robust_execution(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except (MemoryError, RuntimeError) as e:
            logger.critical(f"Critical performance failure in {func.__name__}: {e}")
            return None
        except Exception as e:
            logger.warning(f"Non-fatal disruption during {func.__name__}: {e}")
            return False
    return wrapper

class FrameBufferHandler:
    def __init__(self, limit: int = 60):
        self.limit = limit
        self.queue = []

    @robust_execution
    def process_frame(self, data: Any) -> bool:
        if len(self.queue) >= self.limit:
            raise PerformanceConstraintError("Frame buffer overflow")
        self.queue.append(data)
        return True

    def clear_stale_data(self) -> None:
        try:
            self.queue = self.queue[-self.limit:]
        except Exception:
            self.queue = []