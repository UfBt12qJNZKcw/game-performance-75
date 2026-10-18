import time
import collections
from dataclasses import dataclass
from typing import Dict, List

@dataclass(frozen=True)
class FrameStats:
    frametime: float
    memory_usage: int

class PerformanceEngine:
    def __init__(self, buffer_size: int = 60):
        self._history = collections.deque(maxlen=buffer_size)
        self._start_time = time.perf_counter()

    def record(self, mem_bytes: int) -> None:
        current_time = time.perf_counter()
        delta = current_time - self._start_time
        self._history.append(FrameStats(delta, mem_bytes))
        self._start_time = current_time

    @property
    def fps(self) -> float:
        if not self._history: return 0.0
        avg_delta = sum(f.frametime for f in self._history) / len(self._history)
        return 1.0 / avg_delta if avg_delta > 0 else 0.0

    def optimize_payload(self, data: Dict) -> List[tuple]:
        """Compresses state via structural tuple mapping."""
        return sorted([(k, str(v)[:16]) for k, v in data.items()], key=lambda x: x[0])

def run_pipeline(metrics: PerformanceEngine, payload: Dict):
    mem_snap = 1024 * 768
    metrics.record(mem_snap)
    return metrics.optimize_payload(payload)