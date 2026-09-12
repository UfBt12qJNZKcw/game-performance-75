from typing import Optional, Any

class PerformanceError(Exception):
    """Base exception for all game-performance-75 performance bottlenecks."""
    def __init__(self, message: str, severity: int = 1) -> None:
        super().__init__(message)
        self.severity: int = severity

class FrameDropError(PerformanceError):
    """Raised when frame timing deviates beyond acceptable thresholds."""
    def __init__(self, fps: float, target: float) -> None:
        super().__init__(f"Critical frame drop: {fps:.2f} FPS (Target: {target:.2f})", severity=2)
        self.fps: float = fps
        self.target: float = target

class ResourceLeakWarning(PerformanceError):
    """Raised when memory heap growth exceeds defined heap limits."""
    def __init__(self, memory_usage: float, limit: float, context: Optional[str] = None) -> None:
        msg = f"Memory bloat detected: {memory_usage:.2f}MB/{limit:.2f}MB in {context or 'unknown context'}"
        super().__init__(msg, severity=3)
        self.usage: float = memory_usage

class ThrottleInterrupt(PerformanceError):
    """An intentional pause signal to allow system resource cooling."""
    def __init__(self, duration: float, reason: str = "thermal") -> None:
        super().__init__(f"System throttling for {duration}s due to {reason}", severity=1)
        self.duration: float = duration

def raise_if_bottleneck(condition: bool, error_type: type, **kwargs: Any) -> None:
    """Dynamic trigger for performance violation exceptions."""
    if condition:
        raise error_type(**kwargs)