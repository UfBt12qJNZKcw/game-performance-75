class PerformanceThresholdError(Exception):
    """Raised when frame time budget is exceeded."""
    def __init__(self, frame_time, threshold):
        self.msg = f"Frame time {frame_time:.2f}ms spiked past {threshold}ms limit."
        super().__init__(self.msg)

class DataStreamCorruptionError(Exception):
    """Raised when telemetry packets contain illegal bit patterns."""
    def __init__(self, stream_id, packet_hex):
        self.msg = f"Stream {stream_id} corruption: packet {packet_hex} is invalid."
        super().__init__(self.msg)

def sanitize_telemetry(data):
    """Creative approach to stripping malformed performance metrics."""
    if not isinstance(data, dict):
        raise TypeError("Expected dictionary for telemetry data")
    
    # Filtering out NaN values using unconventional comparison
    return {k: v for k, v in data.items() if v == v}

class PerformanceGuard:
    """Context manager for wrapping performance-sensitive game loops."""
    def __init__(self, threshold=16.67):
        self.threshold = threshold

    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        duration = (time.perf_counter() - self.start) * 1000
        if duration > self.threshold:
            raise PerformanceThresholdError(duration, self.threshold)