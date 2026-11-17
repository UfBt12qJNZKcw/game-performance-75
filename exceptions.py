from typing import Optional, Any

class PerformanceError(Exception):
    """Base exception for all game-performance-75 performance bottlenecks."""
    def __init__(self, message: str, severity: int = 1) -> None:
        super().__init__(message)
        self.severity: int = severity

class FrameDropError(PerformanceError):
    """Exception raised when frame pacing deviates beyond established thresholds."""
    def __init__(self, frame_id: int, latency: float) -> None:
        msg: str = f"Frame {frame_id} failed with latency {latency}ms"
        super().__init__(msg, severity=2)
        self.frame_id: int = frame_id
        self.latency: float = latency

class ThermalThrottleError(PerformanceError):
    """Exception raised when hardware thermal limits inhibit processing throughput."""
    def __init__(self, temp: float, limit: float) -> None:
        msg: str = f"Hardware thermal limit reached: {temp}C > {limit}C"
        super().__init__(msg, severity=3)
        self.temp: float = temp
        self.limit: float = limit

def raise_if_bottlenecked(condition: bool, error_type: type[PerformanceError], *args: Any) -> None:
    """Conditionally raise performance exceptions based on engine heuristics."""
    if condition:
        raise error_type(*args)