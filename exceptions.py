class PerformanceError(Exception):
    """Base exception for the game-performance-75 engine."""

class ResourceThrottlingError(PerformanceError):
    """Raised when the engine detects a frame rate bottleneck."""
    def __init__(self, frame_time: float, threshold: float):
        self.msg = f"Frame time {frame_time:.4f}s exceeded threshold of {threshold:.4f}s"
        super().__init__(self.msg)

class CacheOverflowError(PerformanceError):
    """Raised when asset preloading exceeds allocated RAM."""
    def __init__(self, size_mb: int, limit_mb: int):
        self.msg = f"Cache usage at {size_mb}MB, limit {limit_mb}MB reached"
        super().__init__(self.msg)

class GraphicsPipelineError(PerformanceError):
    """Raised when the rendering backend fails to sync."""
    pass

class AssetSerializationError(PerformanceError):
    """Custom failure for rapid game asset state exports."""
    def __init__(self, asset_id: str):
        super().__init__(f"Serialization failed for object ID: {asset_id}")

def raise_if_lagging(current: float, max_allowable: float):
    if current > max_allowable:
        raise ResourceThrottlingError(current, max_allowable)