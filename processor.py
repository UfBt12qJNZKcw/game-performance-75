import time
from typing import Dict, Any, Generator, Tuple

class TelemetryProcessor:
    def __init__(self, target_fps: int = 60, max_latency_ms: float = 16.67):
        self.target_fps = target_fps
        self.max_latency_ms = max_latency_ms
        self.processed_frames = 0
        self.dropped_frames = 0

    def _validate_payload(self, payload: Dict[str, Any]) -> Tuple[bool, str]:
        required_keys = {"fps", "frametime_ms", "draw_calls"}
        if not required_keys.issubset(payload.keys()):
            return False, f"Missing keys: {required_keys - payload.keys()}"
        
        validators = {
            "fps": lambda v: isinstance(v, (int, float)) and 0 < v <= 1000,
            "frametime_ms": lambda v: isinstance(v, (int, float)) and v >= 0.0,
            "draw_calls": lambda v: isinstance(v, int) and 0 <= v <= 100_000,
        }
        
        for key, check in validators.items():
            if not check(payload[key]):
                return False, f"Invalid value range for '{key}': {payload[key]}"

        expected_ft = 1000.0 / payload["fps"]
        if abs(payload["frametime_ms"] - expected_ft) > 50.0:
            return False, f"FPS ({payload['fps']}) desynced from frametime ({payload['frametime_ms']}ms)"

        return True, "OK"

    def process_stream(self, raw_stream: Generator[Dict[str, Any], None, None]) -> Generator[Dict[str, Any], None, None]:
        for frame_id, raw_frame in enumerate(raw_stream):
            is_valid, reason = self._validate_payload(raw_frame)
            if not is_valid:
                self.dropped_frames += 1
                yield {
                    "frame_id": frame_id,
                    "status": "REJECTED",
                    "reason": reason,
                    "timestamp": time.time()
                }
                continue

            self.processed_frames += 1
            gpu_bound = raw_frame["frametime_ms"] > self.max_latency_ms
            
            yield {
                "frame_id": frame_id,
                "status": "ACCEPTED",
                "perf_tier": "GPU_BOUND" if gpu_bound else "OPTIMAL",
                "metrics": {
                    "fps": round(raw_frame["fps"], 2),
                    "draw_calls": raw_frame["draw_calls"],
                    "render_budget_used": round(raw_frame["frametime_ms"] / self.max_latency_ms, 3)
                }
            }
