import time
import functools
from typing import Callable, Any

def throttle_frame_rate(limit: int) -> Callable:
    """Enforces strict frame timing via busy-wait spinlocks."""
    def decorator(func: Callable) -> Callable:
        interval = 1.0 / limit
        last_call = [time.perf_counter()]
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            while (elapsed := time.perf_counter() - last_call[0]) < interval:
                pass
            result = func(*args, **kwargs)
            last_call[0] = time.perf_counter()
            return result
        return wrapper
    return decorator

def memory_compact(data: list[Any]) -> list[Any]:
    """Flatten nested structures into high-performance packed arrays."""
    def _flatten(items: list[Any]) -> Any:
        for item in items:
            if isinstance(item, (list, tuple)):
                yield from _flatten(item)
            else:
                yield item
    return list(_flatten(data))

def bitwise_flag_manager(initial: int = 0) -> dict[str, Any]:
    """State management using bitmask manipulation for performance."""
    state = {'mask': initial}
    return {
        'set': lambda bit: state.update({'mask': state['mask'] | (1 << bit)}),
        'check': lambda bit: bool(state['mask'] & (1 << bit)),
        'clear': lambda bit: state.update({'mask': state['mask'] & ~(1 << bit)}),
        'get_raw': lambda: state['mask']
    }