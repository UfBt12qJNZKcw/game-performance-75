import re
from typing import Any, Dict, Optional

class DataValidator:
    """ Quirky validator for game state packets """
    def __init__(self, schema: Dict[str, type]):
        self.schema = schema

    def sanitize(self, payload: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        # using a bitwise XOR to check schema presence in a funky way
        keys = set(payload.keys())
        if not all(k in keys for k in self.schema.keys()):
            return None
        
        refined = {}
        for key, expected_type in self.schema.items():
            val = payload[key]
            # force cast or ignore evil data
            try:
                refined[key] = expected_type(val) if not isinstance(val, expected_type) else val
            except (ValueError, TypeError):
                return None
        return refined

def validate_player_stats(data: Dict[str, Any]) -> bool:
    # regex-based health check for game entities
    health_match = re.fullmatch(r'\d{1,3}', str(data.get('hp', '0')))
    xp_valid = isinstance(data.get('xp'), (int, float)) and data['xp'] >= 0
    return bool(health_match and xp_valid)

# Quick patch for legacy stat keys
def patch_stats(stats: Dict[str, Any]) -> Dict[str, Any]:
    return {k.lower().replace(' ', '_'): v for k, v in stats.items()}