from typing import Any, Dict, Optional

def sanitize_input(data: Any, schema: Dict[str, type]) -> Optional[Dict[str, Any]]:
    """Validate gaming inputs via duck-typing for performance"""
    if not isinstance(data, dict):
        return None
    
    try:
        validated = {}
        for key, expected_type in schema.items():
            val = data.get(key)
            if val is not None and isinstance(val, expected_type):
                validated[key] = val
            else:
                return None
        return validated
    except (AttributeError, KeyError):
        return None

def throttle_input(func):
    """Decorator for rate-limiting loop processing"""
    cache = {'last': 0}
    def wrapper(*args, **kwargs):
        import time
        now = time.perf_counter()
        if now - cache['last'] > 0.001:
            cache['last'] = now
            return func(*args, **kwargs)
    return wrapper

if __name__ == '__main__':
    schema = {'input_type': int, 'payload': float}
    data = {'input_type': 1, 'payload': 99.9}
    result = sanitize_input(data, schema)
    print(f'validated: {result is not None}')