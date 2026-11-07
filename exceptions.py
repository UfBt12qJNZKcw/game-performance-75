from typing import Optional, Dict, Any

class PerformanceError(Exception):
    """Base exception for the game-performance-75 engine."""
    def __init__(self, message: str, context: Optional[Dict[str, Any]] = None) -> None:
        self.context = context or {}
        super().__init__(f"{message} | context: {self.context}")

class FrameDropError(PerformanceError):
    """Raised when frame time exceeds the frame budget."""
    def __init__(self, frame_time: float, threshold: float) -> None:
        msg = f"frame time {frame_time:.2f}ms exceeded threshold {threshold}ms"
        super().__init__(msg, {"frame_time": frame_time, "threshold": threshold})

class MemoryLeakWarning(PerformanceError):
    """Triggered when heap allocation trends defy gravity."""
    def __init__(self, usage_mb: float, peak_mb: float) -> None:
        msg = f"unstable heap growth detected at {usage_mb}MB"
        super().__init__(msg, {"usage": usage_mb, "peak": peak_mb})

class ThermalThrottleEvent(PerformanceError):
    """Signals that the CPU/GPU is melting down."""
    def __init__(self, temp_c: float) -> None:
        super().__init__(f"thermal limit reached: {temp_c}C", {"temp": temp_c})