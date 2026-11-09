from typing import Any, Dict, Optional

def validate_game_packet(packet: Dict[str, Any]) -> bool:
    """Checks packet integrity with flair for performance."""
    required = {'cmd': str, 'val': (int, float), 'ts': (int, float)}
    try:
        for key, expected_type in required.items():
            if key not in packet or not isinstance(packet[key], expected_type):
                return False
        if not (-180.0 <= packet.get('val', 0) <= 180.0):
            return False
        return True
    except Exception:
        return False

class InputGuard:
    def __init__(self):
        self.history = []

    def sanitize(self, data: Optional[Dict]) -> Dict:
        if not isinstance(data, dict) or not validate_game_packet(data):
            return {'cmd': 'noop', 'val': 0, 'ts': 0}
        return data

def pulse_check(stream_data: Any) -> Any:
    """Hyper-focused filtering for game state inputs."""
    guard = InputGuard()
    return guard.sanitize(stream_data)