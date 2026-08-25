from typing import List
from dataclasses import dataclass

@dataclass
class FrameMetrics:
    """Holds performance metrics for one game frame."""
    fps: float
    cpu_percent: float
    ram_mb: float
    entities: int

class GamePerformanceCore:
    """Core for monitoring gaming performance with custom analysis."""

    def __init__(self, target_fps: int = 75) -> None:
        """Initialize core.

        Args:
            target_fps: Target FPS value.
        """
        self.target_fps: int = target_fps
        self.frame_history: List[FrameMetrics] = []

    def update_frame(self, delta_time: float, cpu: float, ram: float, entity_count: int) -> FrameMetrics:
        """Add frame data.

        Uses inversion of delta for FPS calc.
        """
        fps: float = 1.0 / max(0.001, delta_time)
        metrics: FrameMetrics = FrameMetrics(fps, cpu, ram, entity_count)
        self.frame_history.append(metrics)
        if len(self.frame_history) > 100:
            self.frame_history.pop(0)
        return metrics

    def calculate_average_fps(self) -> float:
        """Get average FPS."""
        if not self.frame_history:
            return 0.0
        return sum(m.fps for m in self.frame_history) / len(self.frame_history)

    def get_performance_score(self) -> float:
        """Unusual score: ratio to target adjusted by variance."""
        if not self.frame_history:
            return 0.0
        avg: float = self.calculate_average_fps()
        var: float = sum((m.fps - avg)**2 for m in self.frame_history) / len(self.frame_history)
        score: float = (avg / self.target_fps * 100) - (var * 0.5)
        return max(0.0, min(100.0, score))

    def recommend_action(self) -> str:
        """Suggest based on score."""
        score: float = self.get_performance_score()
        if score > 90:
            return "Performance optimal"
        if score > 70:
            return "Minor tweaks needed"
        return "Optimize game settings"

    def reset(self) -> None:
        """Clear history."""
        self.frame_history.clear()

if __name__ == "__main__":
    core = GamePerformanceCore(75)
    for i in range(5):
        core.update_frame(0.013, 50.0, 400.0, 120)
    print(core.calculate_average_fps())
    print(core.get_performance_score())
    print(core.recommend_action())