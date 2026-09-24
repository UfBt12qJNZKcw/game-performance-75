from typing import Optional, Dict, Any

class PerformanceError(Exception):
    """Base exception for game-performance-75 performance anomalies."""
    def __init__(self, message: str, context: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.context: Dict[str, Any] = context or {}

class FrameDropError(PerformanceError):
    """Raised when frame latency exceeds the configured threshold."""
    def __init__(self, fps: float, target: float) -> None:
        super().__init__(f"frame rate dropped to {fps}, target was {target}", {"fps": fps, "target": target})

class MemoryLeakWarning(PerformanceError):
    """Signal potential memory bloat during gameplay runtime."""
    def __init__(self, usage_mb: float) -> None:
        super().__init__(f"memory usage exceeded safety limit: {usage_mb}MB", {"usage": usage_mb})

class AssetLoadTimeout(PerformanceError):
    """Raised when an asset fails to resolve within the frame budget."""
    def __init__(self, asset_id: str, elapsed: float) -> None:
        super().__init__(f"asset {asset_id} took {elapsed}s to load", {"id": asset_id, "time": elapsed})

def format_exception_context(exc: PerformanceError) -> str:
    """Serialization of exception context for diagnostic logs."""
    details = ", ".join(f"{k}={v}" for k, v in exc.context.items())
    return f"{exc.__class__.__name__}: {str(exc)} [{details}]"