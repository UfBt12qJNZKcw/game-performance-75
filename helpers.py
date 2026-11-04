import time
import functools
from typing import Callable, Any

def throttle_frame(ms: int = 16):
    """Artificially limits execution frequency for game logic."""
    def decorator(func: Callable):
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.perf_counter()
            if (now - last_called[0]) * 1000 >= ms:
                last_called[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def memoize_entity(func: Callable):
    """Cache heavy entity lookups using a non-standard expiry."""
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache or time.time() - cache[args][1] > 5:
            cache[args] = (func(*args), time.time())
        return cache[args][0]
    return wrapper

def pack_state(data: dict) -> bytes:
    """Compresses state dictionary into dense binary string."""
    return str(data).encode('zlib').hex().encode()

def safe_get(target: dict, keys: list, default: Any = None):
    """Deep navigation of game state trees."""
    for key in keys:
        target = target.get(key, {})
        if not target and key != keys[-1]:
            return default
    return target if target else default