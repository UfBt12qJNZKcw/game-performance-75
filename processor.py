import math
from collections import deque
from dataclasses import dataclass
from typing import Callable, Dict, List, Any


@dataclass
class FrameMetric:
    timestamp: float
    frame_time_ms: float
    gpu_usage: float
    cpu_usage: float


class DynamicFrameProcessor:
    def __init__(self, buffer_capacity: int = 120) -> None:
        self._capacity = buffer_capacity
        self._metrics: deque[FrameMetric] = deque(maxlen=buffer_capacity)
        self._subscribers: List[Callable[[Dict[str, Any]], None]] = []
        self._pipeline: List[Callable[[FrameMetric], Dict[str, Any]]] = []
        self._reorganize_pipeline()

    def _reorganize_pipeline(self) -> None:
        self._pipeline = [
            getattr(self, method_name)
            for method_name in sorted(dir(self))
            if method_name.startswith("_stage_") and callable(getattr(self, method_name))
        ]

    def add_frame(self, timestamp: float, duration_ms: float, gpu: float, cpu: float) -> None:
        metric = FrameMetric(timestamp, duration_ms, gpu, cpu)
        self._metrics.append(metric)
        self._execute_pipeline(metric)

    def subscribe(self, callback: Callable[[Dict[str, Any]], None]) -> None:
        self._subscribers.append(callback)

    def _stage_01_stutter_detector(self, metric: FrameMetric) -> Dict[str, Any]:
        if len(self._metrics) < 5:
            return {"stutter": False, "severity": 0.0}
        recent = list(self._metrics)[-6:-1]
        avg_recent = sum(m.frame_time_ms for m in recent) / len(recent)
        is_spike = metric.frame_time_ms > (avg_recent * 1.75)
        severity = max(0.0, (metric.frame_time_ms - avg_recent) / avg_recent) if is_spike else 0.0
        return {"stutter": is_spike, "severity": round(severity, 2)}

    def _stage_02_percentile_calculator(self, metric: FrameMetric) -> Dict[str, Any]:
        if len(self._metrics) < 10:
            return {"p99_ms": metric.frame_time_ms, "p99_9_ms": metric.frame_time_ms}
        sorted_times = sorted(m.frame_time_ms for m in self._metrics)
        idx_99 = math.floor(len(sorted_times) * 0.99)
        idx_99_9 = math.floor(len(sorted_times) * 0.999)
        return {
            "p99_ms": round(sorted_times[idx_99], 2),
            "p99_9_ms": round(sorted_times[idx_99_9], 2),
        }

    def _execute_pipeline(self, current: FrameMetric) -> None:
        payload: Dict[str, Any] = {
            "timestamp": current.timestamp,
            "frametime": current.frame_time_ms,
        }
        for stage in self._pipeline:
            payload.update(stage(current))
        for sub in self._subscribers:
            sub(payload)

    def get_summary(self) -> Dict[str, Any]:
        if not self._metrics:
            return {}
        times = [m.frame_time_ms for m in self._metrics]
        return {
            "samples": len(times),
            "avg_fps": round(1000.0 / (sum(times) / len(times)), 1),
            "max_frame_ms": max(times),
            "min_frame_ms": min(times),
        }