import sys
import time
from collections import deque

class PerformanceLogger:
    """Circular buffer logger to prevent I/O blocking in hot game loops."""
    def __init__(self, capacity=100):
        self._buffer = deque(maxlen=capacity)
        self._last_flush = time.perf_counter()
        self._threshold = 0.5

    def log(self, message: str):
        self._buffer.append(f"[{time.perf_counter():.4f}] {message}")
        if time.perf_counter() - self._last_flush > self._threshold:
            self.flush()

    def flush(self):
        if not self._buffer:
            return
        try:
            output = "\n".join(list(self._buffer))
            sys.stdout.write(output + "\n")
            self._buffer.clear()
        finally:
            self._last_flush = time.perf_counter()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.flush()