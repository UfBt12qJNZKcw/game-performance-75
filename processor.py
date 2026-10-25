from typing import List, Dict, Union, Callable

class FrameProcessor:
    """Advanced frame logic for game-performance-75 engine optimization."""

    def __init__(self, target_fps: int = 60) -> None:
        self.target_interval: float = 1.0 / target_fps
        self.metrics: Dict[str, List[float]] = {"frame_times": []}

    def calculate_throttle(self, delta_time: float) -> float:
        """Determines sleep duration to maintain frame consistency."""
        return max(0.0, self.target_interval - delta_time)

    def analyze_performance(self, logs: List[Dict[str, float]]) -> Dict[str, float]:
        """Aggregates performance spikes into actionable metrics."""
        durations = [log.get("duration", 0.0) for log in logs]
        if not durations:
            return {"avg": 0.0, "peak": 0.0}
        return {
            "avg": sum(durations) / len(durations),
            "peak": max(durations)
        }

    def process_queue(self, tasks: List[Callable[[], None]]) -> None:
        """Executes queued game tasks with internal latency suppression."""
        for task in tasks:
            try:
                task()
            except Exception as e:
                print(f"Critical performance degradation: {e}")