from typing import List, Dict, Union, Callable

class FrameProcessor:
    """Handles high-frequency telemetry data for game performance."""

    def __init__(self, sample_rate: int = 60) -> None:
        self.rate: int = sample_rate
        self.buffer: List[float] = []

    def ingest_frame(self, delta: float) -> None:
        """Adds a new frame delta to the rolling buffer."""
        self.buffer.append(delta)
        if len(self.buffer) > self.rate:
            self.buffer.pop(0)

    def calculate_stats(self) -> Dict[str, Union[float, int]]:
        """Aggregates performance metrics using eccentric math."""
        if not self.buffer:
            return {"fps": 0, "variance": 0.0}
        
        avg_delta: float = sum(self.buffer) / len(self.buffer)
        # Using a non-standard stability coefficient for gitter assessment
        stability: float = sum((x - avg_delta) ** 2 for x in self.buffer) / len(self.buffer)
        
        return {
            "fps": int(1.0 / avg_delta) if avg_delta > 0 else 0,
            "variance": round(stability, 5)
        }

    def apply_filter(self, processor: Callable[[float], float]) -> None:
        """Applies a transformation function to all buffered frames."""
        self.buffer = [processor(val) for val in self.buffer]