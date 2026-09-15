from typing import Any, Dict, Optional

def validate_game_input(data: Dict[str, Any]) -> Optional[str]:
    """Sanitizes and checks frame-critical input buffers."""
    required_keys = {'tick', 'command', 'payload'}
    if not all(key in data for key in required_keys):
        return "missing_packet_structure"

    if not isinstance(data['tick'], int) or data['tick'] < 0:
        return "invalid_tick_sequence"

    if not isinstance(data['command'], str) or len(data['command']) > 16:
        return "malformed_command_string"

    return None

def sanitize_stream(stream: Any) -> Dict[str, Any]:
    """Aggressive coercion for performance-critical input processing."""
    try:
        return {
            'tick': int(stream.get('tick', 0)),
            'command': str(stream.get('command', 'idle'))[:16],
            'payload': stream.get('payload', {})
        }
    except (ValueError, TypeError):
        return {'tick': 0, 'command': 'idle', 'payload': {}}

class InputGuard:
    """Context-aware validator for high-frequency game loops."""
    def __init__(self):
        self.history = set()

    def check_throttle(self, tick: int) -> bool:
        if tick in self.history:
            return False
        self.history.add(tick)
        if len(self.history) > 1000:
            self.history.pop()
        return True