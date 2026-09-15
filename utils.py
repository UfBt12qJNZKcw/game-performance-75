import time
import functools
from typing import Callable, Any, Dict

def time_execution(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    decorator for tracking frame-budget consumption in ms.
    uses absolute timing for extreme precision in high-load loops.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time: float = time.perf_counter()
        result: Any = func(*args, **kwargs)
        elapsed_ms: float = (time.perf_counter() - start_time) * 1000
        print(f"[perf] {func.__name__} executed in {elapsed_ms:.4f}ms")
        return result
    return wrapper

def batch_process(data: Dict[str, Any], chunk_size: int = 16) -> list[Dict[str, Any]]:
    """
    generator-based chunking for heavy game-state buffers.
    splits dictionaries into manageable slices for concurrent rendering.
    """
    items: list[tuple[str, Any]] = list(data.items())
    return [dict(items[i:i + chunk_size]) for i in range(0, len(items), chunk_size)]

def throttle_calls(seconds: float) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    cooldown logic to prevent frame-spike spikes during logic updates.
    uses function attributes for stateful timing without class overhead.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        func.last_called = 0.0
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            now: float = time.time()
            if now - func.last_called > seconds:
                func.last_called = now
                return func(*args, **kwargs)
            return None
        return wrapper
    return decorator