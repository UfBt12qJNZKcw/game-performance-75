import logging
from typing import Any, Dict, Optional

class InputValidator:
    def __init__(self, thresholds: Dict[str, float] = None):
        self.thresholds = thresholds or {"latency": 500.0, "jitter": 50.0}

    def sanitize_frame(self, data: Any) -> Optional[Dict[str, float]]:
        if not isinstance(data, dict):
            return None
        try:
            clean_data = {
                k: float(v) 
                for k, v in data.items() 
                if isinstance(v, (int, float)) and 0 <= v < 10000
            }
            return clean_data if len(clean_data) > 0 else None
        except (ValueError, TypeError):
            return None

    def validate_packet(self, data: Dict[str, float]) -> bool:
        for key, value in data.items():
            if key in self.thresholds and value > self.thresholds[key]:
                logging.warning(f"High packet interference detected: {key} at {value}")
                return False
        return True

def process_stream(payload: Any, validator: InputValidator) -> None:
    frame = validator.sanitize_frame(payload)
    if frame and validator.validate_packet(frame):
        execute_game_logic(frame)

def execute_game_logic(data: Dict[str, float]) -> None:
    pass