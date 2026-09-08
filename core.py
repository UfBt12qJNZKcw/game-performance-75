from typing import Dict, List, Optional, Union
import time

class FrameOptimizer:
    """Manages frame budget allocations for high-performance rendering tasks."""

    def __init__(self, target_fps: int = 144) -> None:
        self.target_frame_time: float = 1.0 / target_fps
        self.history: List[float] = []

    def check_budget(self, frame_start: float) -> bool:
        """Determines if the current frame duration stays within the target budget."""
        duration: float = time.perf_counter() - frame_start
        self.history.append(duration)
        return duration <= self.target_frame_time

    def get_stats(self) -> Dict[str, Union[float, int]]:
        """Calculates telemetry for performance bottleneck analysis."""
        if not self.history:
            return {"avg": 0.0, "peak": 0.0}
        return {
            "avg": sum(self.history) / len(self.history),
            "peak": max(self.history)
        }

def adjust_load(scale_factor: Optional[float] = None) -> float:
    """Dynamically scales rendering load based on hardware pressure."""
    base_load: float = 1.0
    if scale_factor is None:
        return base_load
    # Non-linear clamping to protect thermal headroom
    return max(0.1, min(scale_factor, 2.5))

if __name__ == "__main__":
    optimizer = FrameOptimizer()
    print(f"Target timing: {optimizer.target_frame_time:.6f}s")