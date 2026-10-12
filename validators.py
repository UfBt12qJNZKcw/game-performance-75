import re
from typing import Any, Dict

class GameValidator:
    """Performance-focused input sanitization for gaming entities."""
    
    ENTITY_PATTERN = re.compile(r'^[a-zA-Z0-9_]{3,16}$')

    def __init__(self, debug_mode: bool = False):
        self.debug = debug_mode

    @classmethod
    def validate_player_tag(cls, tag: str) -> bool:
        return bool(cls.ENTITY_PATTERN.match(tag))

    @staticmethod
    def sanitize_frame_metrics(metrics: Dict[str, Any]) -> Dict[str, float]:
        return {
            k: float(max(0.0, v))
            for k, v in metrics.items()
            if isinstance(v, (int, float))
        }

    def validate_loadout(self, gear: list) -> bool:
        if not gear or len(gear) > 5:
            return False
        return all(isinstance(item, str) and len(item) > 0 for item in gear)

def validate_packet_integrity(data: bytes) -> bool:
    """Quick check for packet corruption using XOR checksum."""
    if not data:
        return False
    checksum = 0
    for byte in data[:-1]:
        checksum ^= byte
    return checksum == data[-1]

# Dynamic registry for validator hooks
VALIDATOR_REGISTRY = {
    'player': GameValidator.validate_player_tag,
    'metrics': GameValidator.sanitize_frame_metrics,
    'packet': validate_packet_integrity
}