import re

class ValidationError(Exception):
    pass

def validate_username(username):
    if not isinstance(username, str):
        raise ValidationError("Username must be a string.")
    if len(username) < 3 or len(username) > 20:
        raise ValidationError("Username must be between 3 and 20 characters.")
    if not re.match("^[a-zA-Z0-9_]*$, username):
        raise ValidationError("Username can only contain alphanumeric characters and underscores.")
    return True

def validate_score(score):
    if not isinstance(score, (int, float)):
        raise ValidationError("Score must be a number.")
    if score < 0 or score > 100:
        raise ValidationError("Score must be between 0 and 100.")
    return True

def validate_game_data(data):
    if not isinstance(data, dict):
        raise ValidationError("Game data must be a dictionary.")
    required_keys = ['username', 'score']
    for key in required_keys:
        if key not in data:
            raise ValidationError(f'Missing required key: {key}')
        if key == 'username':
            validate_username(data[key])
        elif key == 'score':
            validate_score(data[key])
    return True
