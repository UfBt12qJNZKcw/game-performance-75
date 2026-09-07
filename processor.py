from typing import List, Dict, Union, Optional

class FrameProcessor:
    """Calculates frame jitter and performance overhead metrics for gaming engines."""

    def __init__(self, target_fps: int = 60) -> None:
        self.target_delta: float = 1.0 / target_fps
        self.history: List[float] = []

    def process_frame_times(self, times: List[float]) -> Dict[str, Union[float, str]]:
        """Analyzes raw frame times to return performance health status."""
        if not times:
            return {"status": "idle", "average_jitter": 0.0}

        avg_time: float = sum(times) / len(times)
        jitter: float = abs(avg_time - self.target_delta)
        
        status: str = "stable" if jitter < 0.002 else "unstable"
        
        self.history.append(jitter)
        
        return {
            "status": status,
            "average_jitter": round(jitter, 6),
            "samples": len(times)
        }

    def get_performance_trend(self) -> Optional[float]:
        """Computes moving average of jitter for telemetry logging."""
        if not self.history:
            return None
        return sum(self.history[-10:]) / len(self.history[-10:])

if __name__ == "__main__":
    proc = FrameProcessor()
    report = proc.process_frame_times([0.016, 0.017, 0.0165])
    print(f"Engine Status: {report['status']}")