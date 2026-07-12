import re

def validate_username(username):
    return bool(re.match('^[a-zA-Z0-9_]{3,15}$', username))


def validate_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(regex, email))


def validate_password(password):
    return (len(password) >= 8
            and any(c.isdigit() for c in password)
            and any(c.isupper() for c in password)
            and any(c.islower() for c in password))


def validate_game_id(game_id):
    return isinstance(game_id, int) and game_id > 0


def validate_score(score):
    return isinstance(score, (int, float)) and score >= 0
