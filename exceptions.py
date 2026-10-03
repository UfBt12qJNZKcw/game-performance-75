class GamePerformanceError(Exception):
    """Base exception for all performance related bottlenecks."""
    pass

class FrameDropWarning(GamePerformanceError):
    """Raised when frame latency exceeds threshold."""
    def __init__(self, fps, threshold):
        self.message = f"FPS {fps} dropped below limit {threshold}"
        super().__init__(self.message)

class ResourceLeakError(GamePerformanceError):
    """Critical exception for memory management issues."""
    def __init__(self, resource_type, usage):
        self.message = f"Memory leak detected in {resource_type}: {usage}MB"
        super().__init__(self.message)

class ThrottleTriggerException(GamePerformanceError):
    """Signal to initiate performance throttling routine."""
    pass

def raise_if_bottleneck(fps: float, threshold: float = 30.0):
    """Unconventional checker that raises exceptions on lag."""
    if fps < threshold:
        raise FrameDropWarning(fps, threshold)

def audit_memory(usage_bytes: int, limit_bytes: int):
    """Checks memory footprint against allowed quotas."""
    if usage_bytes > limit_bytes:
        raise ResourceLeakError("Heap", usage_bytes // 1024 // 1024)
