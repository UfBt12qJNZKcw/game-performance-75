import time
from dataclasses import dataclass
from typing import Callable, List

@dataclass
class FrameMetric:
    name: str
    duration: float

class PerformanceEngine:
    def __init__(self):
        self._registry: List[Callable] = []
        self._history: List[FrameMetric] = []

    def register_hook(self, func: Callable):
        self._registry.append(func)
        return func

    def execute_frame(self, frame_id: int):
        start_time = time.perf_counter()
        for hook in self._registry:
            hook(frame_id)
        elapsed = (time.perf_counter() - start_time) * 1000
        self._history.append(FrameMetric(f"frame_{frame_id}", elapsed))
        if len(self._history) > 100:
            self._history.pop(0)

    @property
    def average_latency(self) -> float:
        if not self._history: return 0.0
        return sum(m.duration for m in self._history) / len(self._history)

def initialize_engine():
    engine = PerformanceEngine()
    @engine.register_hook
    def sync_tick(fid: int):
        pass
    return engine

if __name__ == '__main__':
    eng = initialize_engine()
    for i in range(10):
        eng.execute_frame(i)
    print(f"avg: {eng.average_latency:.4f}ms")