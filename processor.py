from typing import List, Dict, Any
class PerformanceProcessor:
    def __init__(self):
        self.min_fps = 1.0
        self.max_latency = 1000.0
        self.errors = []
    def _clamp_value(self, value: float, min_val: float, max_val: float) -> float:
        return max(min_val, min(value, max_val))
    def process(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        if data is None:
            self.errors.append("data is None")
            return {"status": "error", "message": "no data"}
        if not isinstance(data, list):
            self.errors.append("data not list")
            return {"status": "error", "message": "invalid data type"}
        if len(data) == 0:
            self.errors.append("empty data list")
            return {"status": "success", "average_fps": 0, "average_latency": 0, "samples": 0}
        fps_sum = 0.0
        latency_sum = 0.0
        valid_count = 0
        for idx, item in enumerate(data):
            try:
                if not isinstance(item, dict):
                    raise TypeError("item must be dict")
                fps = item.get("fps")
                lat = item.get("latency")
                if fps is None or lat is None:
                    raise KeyError("missing keys")
                fps = float(fps)
                lat = float(lat)
                if fps <= 0 or lat < 0:
                    raise ValueError("invalid performance values")
                fps = self._clamp_value(fps, self.min_fps, 300.0)
                lat = self._clamp_value(lat, 0.0, self.max_latency)
                fps_sum += fps
                latency_sum += lat
                valid_count += 1
            except (TypeError, ValueError, KeyError) as err:
                self.errors.append(f"edge case at {idx}: {type(err).__name__} - {err}")
        if valid_count == 0:
            return {"status": "error", "message": "no valid entries", "errors": self.errors}
        avg_fps = fps_sum / valid_count
        avg_lat = latency_sum / valid_count
        perf_score = (avg_fps * 10) / (avg_lat + 1)
        return {
            "status": "success",
            "average_fps": round(avg_fps, 1),
            "average_latency": round(avg_lat, 1),
            "samples": valid_count,
            "performance_score": round(perf_score, 2),
            "error_count": len(self.errors)
        }