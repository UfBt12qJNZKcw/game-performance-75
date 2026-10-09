from typing import Dict, List, Union, Optional, Callable

class FrameDeltaHandler:
    """Handles frame delta time scaling for consistent game physics."""

    def __init__(self, target_fps: int = 60) -> None:
        self.target_frame_time: float = 1.0 / target_fps
        self.history: List[float] = []

    def calculate_scale(self, current_delta: float) -> float:
        """Computes the multiplier to normalize game speed across frames."""
        if current_delta <= 0:
            return 1.0
        return current_delta / self.target_frame_time

    def smooth_delta(self, new_val: float, window: int = 5) -> float:
        """Applies a rolling average to minimize jitter in physics steps."""
        self.history.append(new_val)
        if len(self.history) > window:
            self.history.pop(0)
        return sum(self.history) / len(self.history)

def process_frame_data(data: Dict[str, Union[int, float]], callback: Optional[Callable[[float], None]] = None) -> float:
    """Processes raw frame input into normalized time coefficients."""
    handler = FrameDeltaHandler()
    raw_delta = float(data.get("delta", 0.016))
    smoothed = handler.smooth_delta(raw_delta)
    scale = handler.calculate_scale(smoothed)

    if callback:
        callback(scale)

    return scale