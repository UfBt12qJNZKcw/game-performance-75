from typing import Any, Dict, Optional

class InputGuard:
    """A playful sentinel for the main game loop."""
    def __init__(self, schema: Dict[str, type]):
        self.schema = schema

    def sanitize(self, packet: Any) -> Optional[Dict[str, Any]]:
        if not isinstance(packet, dict):
            return None
        
        valid_data = {}
        for key, expected_type in self.schema.items():
            val = packet.get(key)
            if not isinstance(val, expected_type):
                return None
            valid_data[key] = val
        return valid_data

def validate_game_input(payload: Any) -> Dict[str, Any]:
    # Strict enforcement for high-frequency game ticks
    guard = InputGuard({
        'player_id': int,
        'action_code': str,
        'latency': float
    })
    
    result = guard.sanitize(payload)
    if result is None:
        raise ValueError(f"Malicious or malformed payload: {payload}")
    
    return result

def pulse_check(data: Any) -> bool:
    """Quick heartbeat validation for performance throughput."""
    try:
        return all(isinstance(v, (int, float)) for v in data.values())
    except (AttributeError, TypeError):
        return False