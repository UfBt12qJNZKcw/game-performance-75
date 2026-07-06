import re

def validate_player_name(name):
    if not isinstance(name, str):
        return False
    return bool(re.match('^[A-Za-z0-9_]{3,16}$', name))

def validate_score(score):
    return isinstance(score, int) and score >= 0

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_regex, email))

def validate_game_data(data):
    if not isinstance(data, dict):
        return False
    required_keys = ['player_name', 'score', 'email']
    for key in required_keys:
        if key not in data:
            return False
    return (validate_player_name(data['player_name']) and
            validate_score(data['score']) and
            validate_email(data['email']))

if __name__ == '__main__':
    test_data = {
        'player_name': 'Gamer123',
        'score': 100,
        'email': 'gamer@example.com'
    }
    print(validate_game_data(test_data))  # Should return True