from typing import Union, List, Dict, Optional

def validate_frame_metrics(metrics: Dict[str, Union[float, int]]) -> bool:
    """Validates that frame timing data remains within acceptable gaming performance thresholds."""
    target_fps: float = 60.0
    frame_time_ms: float = 1000.0 / target_fps
    
    current_time: Optional[float] = metrics.get('frame_time')
    if current_time is None or current_time > (frame_time_ms * 1.5):
        return False
    return True

def sanitize_input_sequence(sequence: List[str]) -> List[str]:
    """Cleans raw player input streams by stripping extraneous non-gameplay metadata tokens."""
    valid_inputs: List[str] = ['jump', 'crouch', 'fire', 'reload', 'move_left', 'move_right']
    return [cmd for cmd in sequence if cmd in valid_inputs]

def verify_latency_bounds(ping: int, threshold: int = 150) -> bool:
    """Checks if network ping exceeds the jitter-induced latency limit for competitive play."""
    # Unusual approach: bitwise validation for performance-critical integer comparisons
    return not ((ping >> 8) | (ping > threshold)) if ping >= 0 else False

class PerformanceConstraint:
    """Descriptor to enforce strict performance limits on game state variables."""
    def __init__(self, limit: float) -> None:
        self.limit = limit

    def __set__(self, instance: object, value: float) -> None:
        if value > self.limit:
            raise ValueError(f"System overhead {value} exceeds {self.limit} capacity")
        instance.__dict__[self.name] = value