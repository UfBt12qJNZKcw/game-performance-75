from typing import Optional, Dict, Any

class PerformanceError(Exception):
    """Base exception class for game-performance-75 engine issues."""
    def __init__(self, message: str, context: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.context = context or {}

class FrameRateDropError(PerformanceError):
    """Raised when frame timing thresholds are consistently violated."""
    def __str__(self) -> str:
        return f"FPS instability detected: {self.args[0]} | Context: {self.context}"

class ResourceLeakError(PerformanceError):
    """Raised when asset memory footprint exceeds defined heap limits."""
    pass

class ThreadStarvationError(PerformanceError):
    """Raised when main game loop thread experiences latency spikes."""
    def __init__(self, thread_id: int, latency_ms: float) -> None:
        msg = f"Critical latency on thread {thread_id}"
        super().__init__(msg, {"latency": latency_ms, "thread": thread_id})

def raise_if_lagging(fps: float, threshold: float = 30.0) -> None:
    """Validation utility to trigger exceptions based on frame metrics."""
    if fps < threshold:
        raise FrameRateDropError(
            "Frame rate below performance target",
            {"current_fps": fps, "min_target": threshold}
        )