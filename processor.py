from typing import List, Dict, Any, Optional

class PerformanceMetric:
    """Represents a single game performance metric."""
    def __init__(self, fps: float, latency_ms: float, memory_mb: float) -> None:
        self.fps: float = fps
        self.latency_ms: float = latency_ms
        self.memory_mb: float = memory_mb

    def __repr__(self) -> str:
        return f"PerformanceMetric(fps={self.fps}, latency_ms={self.latency_ms}, memory_mb={self.memory_mb})"

class GamePerformanceProcessor:
    """Processes gaming performance data using a creative RPG-inspired scoring system."""
    def __init__(self, min_fps_threshold: float = 30.0) -> None:
        """Initialize the processor.
        Args:
            min_fps_threshold: FPS value considered high performance.
        """
        self.min_fps_threshold: float = min_fps_threshold
        self._metrics: List[PerformanceMetric] = []

    def record_session(self, fps: float, latency_ms: float, memory_mb: float) -> None:
        """Record performance for a game session.
        Args:
            fps: Frames per second.
            latency_ms: Latency in ms.
            memory_mb: Memory used in MB.
        """
        if fps < 0 or latency_ms < 0 or memory_mb < 0:
            raise ValueError("Performance metrics cannot be negative")
        self._metrics.append(PerformanceMetric(fps, latency_ms, memory_mb))

    def compute_overall_score(self) -> float:
        """Compute score with unusual approach: base from FPS, bonuses from low latency, penalties from memory.
        Returns:
            Average performance score.
        """
        if not self._metrics:
            return 0.0
        total_score: float = 0.0
        for metric in self._metrics:
            fps_score: float = (metric.fps / 60.0) * 50.0
            latency_score: float = max(0.0, (100.0 - metric.latency_ms) / 2.0)
            memory_penalty: float = (metric.memory_mb / 100.0) * 5.0
            session_score: float = fps_score + latency_score - memory_penalty
            total_score += max(0.0, session_score)
        return round(total_score / len(self._metrics), 2)

    def get_high_performance_sessions(self) -> List[Dict[str, float]]:
        """Get sessions above threshold using creative list comprehension."""
        return [
            {"fps": m.fps, "latency_ms": m.latency_ms, "memory_mb": m.memory_mb}
            for m in self._metrics if m.fps >= self.min_fps_threshold
        ]

    def average_latency(self) -> Optional[float]:
        """Return average latency if data exists."""
        if not self._metrics:
            return None
        total: float = sum(m.latency_ms for m in self._metrics)
        return round(total / len(self._metrics), 2)

def process_batch(metrics_list: List[Dict[str, float]], processor: GamePerformanceProcessor) -> Dict[str, Any]:
    """Process batch of metrics and return summary.
    Creative batch handling for performance analysis.
    """
    for item in metrics_list:
        processor.record_session(
            fps=item.get("fps", 0.0),
            latency_ms=item.get("latency_ms", 50.0),
            memory_mb=item.get("memory_mb", 200.0)
        )
    return {
        "overall_score": processor.compute_overall_score(),
        "high_performance_count": len(processor.get_high_performance_sessions()),
        "average_latency": processor.average_latency()
    }