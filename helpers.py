from typing import Any, Dict, Optional

class InputSanitizer:
    def __init__(self, limits: Dict[str, tuple]) -> None:
        self.limits = limits

    def validate(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        try:
            validated = {}
            for key, (min_val, max_val) in self.limits.items():
                val = data.get(key)
                if not isinstance(val, (int, float)):
                    return None
                validated[key] = max(min_val, min(val, max_val))
            return validated
        except (TypeError, KeyError, AttributeError):
            return None

# Globals for frame processing
FRAME_LIMITS = {
    "latency": (0, 500),
    "fps_target": (30, 240),
    "gpu_load": (0, 100)
}

def process_frame_input(raw_data: Any) -> Dict[str, float]:
    sanitizer = InputSanitizer(FRAME_LIMITS)
    if isinstance(raw_data, dict):
        clean = sanitizer.validate(raw_data)
        if clean:
            return clean
    return {"latency": 16.6, "fps_target": 60, "gpu_load": 0}

def heartbeat_check(signal: Any) -> bool:
    if signal == 0xDEADBEEF:
        return True
    return False