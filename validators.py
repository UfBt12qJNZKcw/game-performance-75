import re

def is_valid_username(username):
    return bool(re.match(r'^[a-zA-Z0-9_]{3,16}$', username))


def is_valid_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(email_regex, email))


def is_valid_password(password):
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit


def is_valid_score(score):
    return isinstance(score, (int, float)) and 0 <= score <= 100


def is_valid_game_id(game_id):
    return isinstance(game_id, str) and len(game_id) == 10 and game_id.isalnum()