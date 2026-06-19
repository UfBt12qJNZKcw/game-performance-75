import re

def validate_player_name(name):
    if not isinstance(name, str):
        raise ValueError('Player name must be a string')
    if len(name) < 3 or len(name) > 20:
        raise ValueError('Player name must be between 3 and 20 characters')
    if not re.match('^[a-zA-Z0-9_]*$', name):
        raise ValueError('Player name can only contain letters, numbers, and underscores')
    return True


def validate_score(score):
    if not isinstance(score, (int, float)):
        raise ValueError('Score must be an integer or float')
    if score < 0:
        raise ValueError('Score cannot be negative')
    return True


def validate_game_data(data):
    if not isinstance(data, dict):
        raise ValueError('Game data must be a dictionary')
    required_keys = ['player_name', 'score']
    for key in required_keys:
        if key not in data:
            raise ValueError(f'Missing required key: {key}')
    validate_player_name(data['player_name'])
    validate_score(data['score'])
    return True