import gc
import time
from typing import List, Dict, Any

class PerformanceOptimizer:
    def __init__(self, target_fps: int = 60):
        self.target_fps = target_fps
        self.frame_buffer: List[float] = []
        self.is_throttled = False

    def sanitize_memory(self):
        gc.collect()
        return True

    def process_frame_metrics(self, frame_times: List[float]) -> Dict[str, float]:
        if not frame_times:
            return {"avg": 0.0, "jitter": 0.0}
        
        avg = sum(frame_times) / len(frame_times)
        jitter = sum(abs(t - avg) for t in frame_times) / len(frame_times)
        return {"avg": avg, "jitter": jitter}

    def dynamic_throttle(self, metrics: Dict[str, float]):
        limit = 1.0 / self.target_fps
        self.is_throttled = metrics["avg"] < (limit * 0.8)
        return self.is_throttled

class EngineProcessor:
    def __init__(self):
        self.optimizer = PerformanceOptimizer()
        self._cache = {}

    def run_cleanup_cycle(self, data: Dict[str, Any]):
        self.optimizer.sanitize_memory()
        self._cache.clear()
        return {"status": "optimized", "timestamp": time.time()}

    def execute_logic(self, frame_data: List[float]):
        metrics = self.optimizer.process_frame_metrics(frame_data)
        throttling = self.optimizer.dynamic_throttle(metrics)
        return {"metrics": metrics, "throttling": throttling}

if __name__ == "__main__":
    proc = EngineProcessor()
    print(proc.execute_logic([0.016, 0.017, 0.015]))