import re

def validate_username(username):
    if not isinstance(username, str) or len(username) < 3:
        return False
    return re.match(r'^[a-zA-Z0-9_.]+$', username) is not None


def validate_email(email):
    if not isinstance(email, str):
        return False
    return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) is not None


def validate_password(password):
    if len(password) < 8:
        return False
    return (re.search(r'[A-Za-z]', password) and 
            re.search(r'[0-9]', password) and 
            re.search(r'[@$!%*?&]', password)) is not None


def validate_age(age):
    return isinstance(age, int) and 0 < age < 120


def validate_game_score(score):
    return isinstance(score, (int, float)) and 0 <= score <= 100