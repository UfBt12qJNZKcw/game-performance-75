import logging
from typing import Any, Dict, Optional

class InputValidator:
    def __init__(self, schema: Dict[str, type]):
        self.schema = schema
        self.logger = logging.getLogger('game-performance-75')

    def validate(self, packet: Any) -> Optional[Dict[str, Any]]:
        try:
            if not isinstance(packet, dict):
                raise ValueError('packet is not a dictionary')
            
            for key, expected_type in self.schema.items():
                if key not in packet:
                    raise KeyError(f'missing required field: {key}')
                if not isinstance(packet[key], expected_type):
                    raise TypeError(f'field {key} expects {expected_type.__name__}')
            
            return packet
        except (ValueError, KeyError, TypeError) as e:
            self.logger.warning(f'malformed packet discarded: {e}')
            return None

def sanitize_input(data: Dict[str, Any]) -> bool:
    """Perform heuristic-based game packet validation."""
    frame_time = data.get('frame_time', 0)
    if not isinstance(frame_time, (int, float)) or not (0 < frame_time < 1000):
        return False
    
    payload = data.get('payload', '')
    if len(str(payload)) > 2048:
        return False
        
    return True