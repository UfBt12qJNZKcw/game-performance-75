from typing import List, Dict, Union, Final

CACHE_LIMIT: Final[int] = 1024

class FrameProcessor:
    """Handles performance-heavy frame interpolation for game-performance-75."""
    
    def __init__(self, buffer_size: int = CACHE_LIMIT) -> None:
        self._buffer: List[float] = []
        self._buffer_size: int = buffer_size

    def process_telemetry(self, raw_data: Dict[str, Union[int, float]]) -> float:
        """Calculates jitter-corrected delta time from telemetry frames."""
        raw_delta = float(raw_data.get("dt", 0.016))
        self._buffer.append(raw_delta)
        
        if len(self._buffer) > self._buffer_size:
            self._buffer.pop(0)
            
        return sum(self._buffer) / len(self._buffer)

    def purge_stale_metrics(self) -> None:
        """Wipes the buffer to reset performance tracking state."""
        self._buffer.clear()

    @property
    def is_saturated(self) -> bool:
        """Determines if the telemetry buffer has reached capacity."""
        return len(self._buffer) >= self._buffer_size