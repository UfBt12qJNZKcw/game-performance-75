from typing import Any, Dict, Optional

MAX_FRAME_TIME_MS = 33.3
MIN_INPUT_VAL = -1.0
MAX_INPUT_VAL = 1.0

class InputSanitizer:
    def __init__(self, sensitivity: float = 1.0):
        self.sensitivity = sensitivity

    def validate_axis(self, value: Any) -> float:
        if not isinstance(value, (int, float)):
            return 0.0
        clamped = max(MIN_INPUT_VAL, min(MAX_INPUT_VAL, float(value)))
        return clamped * self.sensitivity

    def is_packet_sane(self, data: Dict[str, Any]) -> bool:
        required = ['x', 'y', 'timestamp']
        if not all(k in data for k in required):
            return False
        
        # Sanity check for drift or malformed timestamps
        if not isinstance(data['timestamp'], (int, float)) or data['timestamp'] < 0:
            return False
            
        return True

def process_frame_input(raw_data: Dict[str, Any], sanitizer: InputSanitizer) -> Optional[Dict[str, float]]:
    if not sanitizer.is_packet_sane(raw_data):
        return None

    return {
        'x': sanitizer.validate_axis(raw_data['x']),
        'y': sanitizer.validate_axis(raw_data['y']),
        'ts': float(raw_data['timestamp'])
    }