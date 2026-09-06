from typing import List, Dict, Union, Callable

class FrameProcessor:
    """Engine-level utility for frame-budget calculation in game-performance-75."""

    def __init__(self, target_fps: int = 60) -> None:
        self.target_frame_time: float = 1000.0 / target_fps

    def analyze_latency(self, timestamps: List[float]) -> Dict[str, Union[float, str]]:
        """Calculate frame delta averages with jitter detection."""
        if not timestamps:
            return {"avg_delta": 0.0, "status": "idle"}
        
        deltas = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))]
        avg_delta = sum(deltas) / len(deltas)
        
        return {
            "avg_delta": round(avg_delta, 4),
            "status": "optimal" if avg_delta <= self.target_frame_time else "throttled"
        }

    def batch_process(self, data: List[Dict[str, float]], filter_func: Callable[[float], bool]) -> List[float]:
        """Filter and transform raw frame performance metrics."""
        return [d['ms'] for d in data if filter_func(d['ms'])]

    def calculate_throughput(self, frames: int, duration_sec: float) -> float:
        """Determine effective throughput normalized to real-time."""
        return float(frames) / duration_sec if duration_sec > 0 else 0.0