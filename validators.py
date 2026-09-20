import functools

class InputSanitizer:
    def __init__(self, schema):
        self.schema = schema

    def validate(self, data):
        for key, validator in self.schema.items():
            val = data.get(key)
            if not validator(val):
                raise ValueError(f'invalid input detected: {key}')
        return True

def validate_game_state(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        data = args[0] if args else kwargs.get('data')
        if not isinstance(data, dict) or 'frame_id' not in data:
            return None
        if data.get('frame_id', 0) < 0:
            return None
        return func(*args, **kwargs)
    return wrapper

SCHEMA = {
    'player_x': lambda x: isinstance(x, (int, float)) and -1000 <= x <= 1000,
    'player_y': lambda x: isinstance(x, (int, float)) and -1000 <= x <= 1000,
    'action_code': lambda x: x in ['MOVE', 'JUMP', 'ATTACK']
}

def process_frame_input(data):
    sanitizer = InputSanitizer(SCHEMA)
    try:
        if sanitizer.validate(data):
            return True
    except ValueError:
        return False
    return False