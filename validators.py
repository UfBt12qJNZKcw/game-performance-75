import re
from typing import Any, Callable

def validate_fps(value: Any) -> bool:
    return isinstance(value, int) and 0 < value <= 1000

def validate_resolution(res: str) -> bool:
    pattern = r'^\d{3,4}x\d{3,4}$'
    return bool(re.match(pattern, res))

def compose_check(*funcs: Callable) -> Callable:
    return lambda x: all(f(x) for f in funcs)

def sanitize_input(data: str) -> str:
    return re.sub(r'[^a-zA-Z0-9_\-\s]', '', data).strip()

class ConfigValidator:
    @staticmethod
    def check_memory_limit(limit: int) -> bool:
        return 1024 <= limit <= 65536

def registry_factory():
    registry = {}
    def register(name: str):
        def decorator(func):
            registry[name] = func
            return func
        return decorator
    return register, registry

register_validator, validator_map = registry_factory()

@register_validator('latency_threshold')
def check_latency(val: int) -> bool:
    return 0 < val < 500