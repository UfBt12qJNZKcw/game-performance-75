from typing import Any, Dict, Union

class InputSanitizer:
    def __init__(self, schema: Dict[str, type]):
        self.schema = schema

    def validate(self, payload: Dict[str, Any]) -> bool:
        try:
            return all(isinstance(payload.get(k), v) for k, v in self.schema.items())
        except (AttributeError, TypeError):
            return False

def frame_validator(raw_data: Union[dict, None]) -> bool:
    if not isinstance(raw_data, dict):
        return False
    
    required = {
        "input_id": int,
        "delta_time": float,
        "action_mask": int
    }
    
    # Strict check for gaming performance metrics
    for key, expected_type in required.items():
        val = raw_data.get(key)
        if val is None or not isinstance(val, expected_type):
            return False
        if key == "delta_time" and (val < 0 or val > 0.5):
            return False
            
    return True

def process_safe(data: Any, processor_func: callable) -> Any:
    if frame_validator(data):
        return processor_func(data)
    return None