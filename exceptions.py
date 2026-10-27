class PerformanceThresholdError(Exception):
    """Raised when game metrics drop below acceptable thresholds."""
    def __init__(self, metric, value, threshold):
        self.message = f"Critical {metric} drop: {value} (min: {threshold})"
        super().__init__(self.message)

class ResourceLeakWarning(Warning):
    """Non-fatal warning for potential memory or object leaks."""
    pass

class HardwareAbstractionError(Exception):
    """Raised when low-level driver calls fail during frame rendering."""
    pass

def raise_if_laggy(fps, target=60):
    if fps < target:
        raise PerformanceThresholdError("FPS", fps, target)

class ErrorFactory:
    @staticmethod
    def critical_shutdown(reason):
        return RuntimeError(f"[CRITICAL] {reason.upper()} - Terminating Engine")

def safe_execute(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        return ErrorFactory.critical_shutdown(str(e))

__all__ = ['PerformanceThresholdError', 'ResourceLeakWarning', 'HardwareAbstractionError', 'raise_if_laggy', 'ErrorFactory', 'safe_execute']