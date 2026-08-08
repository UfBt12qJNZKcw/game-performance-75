import re

class ValidationError(Exception):
    pass

def validate_username(username):
    if not isinstance(username, str) or not username:
        raise ValidationError('Username must be a non-empty string.')
    if len(username) < 3 or len(username) > 20:
        raise ValidationError('Username must be between 3 and 20 characters long.')
    if not re.match('^[a-zA-Z0-9_]+$', username):
        raise ValidationError('Username can only contain letters, numbers, and underscores.')
    return True


def validate_score(score):
    if not isinstance(score, int) or score < 0:
        raise ValidationError('Score must be a non-negative integer.')
    return True


def validate_email(email):
    if not isinstance(email, str) or not email:
        raise ValidationError('Email must be a non-empty string.')
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        raise ValidationError('Invalid email format.')
    return True
