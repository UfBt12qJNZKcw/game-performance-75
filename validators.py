def validate_player_name(name):
    if not isinstance(name, str):
        raise TypeError('Player name must be a string')
    if len(name) == 0:
        raise ValueError('Player name cannot be empty')
    if len(name) > 20:
        raise ValueError('Player name cannot exceed 20 characters')
    if any(char in name for char in ['!', '@', '#', '$', '%', '^', '&', '*']):
        raise ValueError('Player name contains invalid characters')
    return True

def validate_score(score):
    if not isinstance(score, (int, float)):
        raise TypeError('Score must be an integer or float')
    if score < 0:
        raise ValueError('Score cannot be negative')
    return True

def validate_game_mode(mode):
    valid_modes = ['easy', 'medium', 'hard']
    if mode not in valid_modes:
        raise ValueError(f'Invalid game mode. Choose from {valid_modes}')
    return True

# Example usage
try:
    validate_player_name('Player123')  
    validate_score(100)  
    validate_game_mode('easy')
except (TypeError, ValueError) as e:
    print(e)