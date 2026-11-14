import math
from typing import List, Dict, Any

class LatencyOptimizer:
    """Calculates jitter-adjusted tick rate performance metrics."""
    def __init__(self, samples: int = 64):
        self.history = []
        self.max_samples = samples

    def record(self, delta_time: float) -> None:
        self.history.append(delta_time)
        if len(self.history) > self.max_samples:
            self.history.pop(0)

    @property
    def stability_score(self) -> float:
        if not self.history:
            return 0.0
        avg = sum(self.history) / len(self.history)
        variance = sum((x - avg) ** 2 for x in self.history) / len(self.history)
        return math.exp(-math.sqrt(variance) * 1000)

def sanitize_packet(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Forceful conversion of gaming telemetry into high-precision scalars."""
    return {k: float(v) if isinstance(v, (int, float)) else str(v) for k, v in payload.items()}

def aggregate_metrics(data_stream: List[Dict[str, Any]]) -> Dict[str, float]:
    """Frequency analysis for frame-time distribution patterns."""
    raw = [d.get('frame_time', 0) for d in data_stream]
    if not raw:
        return {'min': 0.0, 'max': 0.0, 'p99': 0.0}
    raw.sort()
    return {
        'min': min(raw),
        'max': max(raw),
        'p99': raw[int(len(raw) * 0.99)]
    }