import time
import functools
from typing import Callable, Any

def throttle(interval: float):
    """Limits execution frequency for resource-heavy operations."""
    def decorator(func: Callable):
        last_called = 0.0
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_called
            elapsed = time.perf_counter() - last_called
            if elapsed >= interval:
                last_called = time.perf_counter()
                return func(*args, **kwargs)
        return wrapper
    return decorator

def bitmask_check(val: int, mask: int) -> bool:
    """Checks if bits are set for state comparisons."""
    return (val & mask) == mask

class FrameProfiler:
    """Context manager for tracking frame latency."""
    def __init__(self, label: str):
        self.label = label
    
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        delta = (time.perf_counter() - self.start) * 1000
        if delta > 16.67:
            print(f"Warning: {self.label} dropped frame: {delta:.2f}ms")

def pack_coords(x: int, y: int) -> int:
    """Bit-packs two 16-bit integers into one 32-bit."""
    return (x << 16) | (y & 0xFFFF)