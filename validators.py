import re
from typing import Any, Callable, Dict

def validate_fps_range(value: Any) -> bool:
    return isinstance(value, int) and 0 < value <= 480

def validate_packet_loss(value: float) -> bool:
    return 0.0 <= value <= 1.0

def validate_gamertag(tag: str) -> bool:
    pattern = re.compile(r'^[a-zA-Z0-9_]{3,16}$')
    return bool(pattern.match(tag))

class ConfigValidator:
    def __init__(self, schema: Dict[str, Callable[[Any], bool]]):
        self.schema = schema

    def check(self, data: Dict[str, Any]) -> Dict[str, bool]:
        results = {}
        for key, validator in self.schema.items():
            results[key] = validator(data.get(key))
        return results

# Helper instances for common perf checks
game_validators = ConfigValidator({
    'fps_limit': validate_fps_range,
    'max_ping': lambda x: isinstance(x, int) and x < 500,
    'packet_loss_threshold': validate_packet_loss
})