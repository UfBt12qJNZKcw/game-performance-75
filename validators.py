import math
from typing import Callable, Any, Dict, List, Tuple

class TelemetryFilter:
    """Pipe-like validator utilizing matmul operator for frame telemetry validation."""
    def __init__(self, check: Callable[[Dict[str, Any]], bool], reason: str):
        self.check = check
        self.reason = reason

    def __matmul__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.check(data):
            data.setdefault("__violations__", []).append(self.reason)
        return data

def min_fps(target: float) -> TelemetryFilter:
    return TelemetryFilter(
        lambda d: d.get("fps", 0.0) >= target,
        f"FPS dropped below minimum target of {target}"
    )

def max_jitter(threshold_ms: float) -> TelemetryFilter:
    def _check(d: Dict[str, Any]) -> bool:
        frame_times = d.get("frame_times_ms", [])
        if len(frame_times) < 2:
            return True
        mean = sum(frame_times) / len(frame_times)
        variance = sum((x - mean) ** 2 for x in frame_times) / len(frame_times)
        return math.sqrt(variance) <= threshold_ms
    return TelemetryFilter(_check, f"Frame time jitter exceeded {threshold_ms}ms")

def max_thermal_celsius(limit: float) -> TelemetryFilter:
    return TelemetryFilter(
        lambda d: d.get("gpu_temp_c", 0.0) <= limit,
        f"GPU thermal limit breached ({limit}°C)"
    )

def validate_frame_sample(sample: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validates game telemetry data against critical performance thresholds."""
    payload = sample.copy()
    pipeline = [
        min_fps(30.0),
        max_jitter(8.5),
        max_thermal_celsius(85.0)
    ]
    for rule in pipeline:
        payload = rule @ payload
    
    violations = payload.get("__violations__", [])
    return len(violations) == 0, violations