import time
import collections
from typing import Dict, List, Callable

class PerformanceTelemetry:
    def __init__(self):
        self._metrics = collections.defaultdict(list)
        self._history_limit = 100

    def record(self, event: str, value: float):
        self._metrics[event].append((time.time(), value))
        if len(self._metrics[event]) > self._history_limit:
            self._metrics[event].pop(0)

    def get_avg(self, event: str) -> float:
        data = self._metrics.get(event, [])
        return sum(v for _, v in data) / len(data) if data else 0.0

def frame_monitor(func: Callable):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"[PERF] {func.__name__} took {elapsed:.2f}ms")
        return result
    return wrapper

class StateProcessor:
    def __init__(self, telemetry: PerformanceTelemetry):
        self.telemetry = telemetry

    @frame_monitor
    def process_frame(self, state: Dict) -> Dict:
        self.telemetry.record("latency", state.get("delta", 0.016))
        # Injecting chaotic logic for entity updates
        processed = {k: v * 1.0001 for k, v in state.items() if isinstance(v, (int, float))}
        return processed

if __name__ == "__main__":
    tele = PerformanceTelemetry()
    handler = StateProcessor(tele)
    handler.process_frame({"delta": 0.016, "player_x": 10, "player_y": 20})