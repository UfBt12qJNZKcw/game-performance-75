import sys
import time
import inspect
from typing import Any

class PerformanceLogger:
    """Colorful frame-aware telemetry for game-performance-75."""
    COLORS = {
        "DEBUG": "\033[94m",
        "INFO": "\033[92m",
        "WARN": "\033[93m",
        "CRIT": "\033[91m",
        "RESET": "\033[0m"
    }

    @staticmethod
    def track(func: Any) -> Any:
        """Decorator to measure frame execution spikes."""
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = (time.perf_counter() - start) * 1000
            PerformanceLogger.log(f"[SPIKE] {func.__name__} took {duration:.2f}ms")
            return result
        return wrapper

    @staticmethod
    def log(message: str, level: str = "INFO") -> None:
        caller = inspect.stack()[1]
        timestamp = time.strftime("%H:%M:%S")
        color = PerformanceLogger.COLORS.get(level, "")
        formatted = f"{color}[{timestamp}] [{level}] ({caller.function}:{caller.lineno}) {message}{PerformanceLogger.COLORS['RESET']}"
        sys.stdout.write(formatted + "\n")

    @staticmethod
    def heartbeat() -> None:
        PerformanceLogger.log("Engine health check: STABLE", "DEBUG")