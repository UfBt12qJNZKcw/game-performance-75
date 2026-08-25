import time

class GameException(Exception):
    """Base class for game exceptions with timestamp and performance data."""
    def __init__(self, message, performance_data=None):
        super().__init__(message)
        self.timestamp = time.time()
        self.performance_data = performance_data or {}
    def get_diagnostics(self):
        return {
            "timestamp": self.timestamp,
            "exception_type": self.__class__.__name__,
            "message": str(self),
            "performance": self.performance_data
        }

class LowFPSException(GameException):
    """Exception for when FPS is below acceptable levels."""
    def __init__(self, current_fps, min_fps=30):
        message = f"Low FPS detected: {current_fps} (minimum: {min_fps})"
        super().__init__(message, {"current_fps": current_fps, "min_fps": min_fps})
        self.current_fps = current_fps
        self.min_fps = min_fps
    def suggest_optimization(self):
        """Unusual creative approach: suggest based on data."""
        if self.current_fps < 10:
            return "Reduce resolution or disable effects"
        return "Lower graphics settings temporarily"

class MemoryOverflowException(GameException):
    """For when memory usage exceeds limits in gaming."""
    def __init__(self, used_mb, limit_mb=2048):
        message = f"Memory overflow: {used_mb}MB used, limit {limit_mb}MB"
        super().__init__(message, {"used_mb": used_mb, "limit_mb": limit_mb})
        self.used_mb = used_mb
        self.limit_mb = limit_mb

class InputDelayException(Exception):
    """Simple exception for input delays."""
    def __init__(self, delay_ms):
        super().__init__(f"Excessive input delay: {delay_ms}ms")
        self.delay_ms = delay_ms

COMMON_EXCEPTIONS = {
    "low_fps": LowFPSException,
    "memory": MemoryOverflowException,
    "input_delay": InputDelayException
}

def create_game_exception(exc_type, *args):
    """Helper function to create exception instances creatively."""
    if exc_type in COMMON_EXCEPTIONS:
        return COMMON_EXCEPTIONS[exc_type](*args)
    return GameException(f"Unknown game error: {exc_type}")

def handle_performance_error(error):
    """Unusual handler that returns diagnostic info."""
    if isinstance(error, GameException):
        return error.get_diagnostics()
    return {"error": str(error)}

def monitor_game_performance(fps, memory_mb):
    if fps < 30:
        exc = create_game_exception("low_fps", fps, 30)
        raise exc
    if memory_mb > 2048:
        exc = create_game_exception("memory", memory_mb, 2048)
        raise exc