import re

def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def is_positive_integer(value: int) -> bool:
    return isinstance(value, int) and value > 0


def is_valid_username(username: str) -> bool:
    return bool(re.match('^[a-zA-Z0-9_]{3,20}$', username))


def is_valid_password(password: str) -> bool:
    return (len(password) >= 8 and
            any(char.isdigit() for char in password) and
            any(char.isalpha() for char in password) and
            any(char in '!@#$%^&*()-+' for char in password))


def validate_inputs(email: str, age: int, username: str, password: str) -> dict:
    errors = {}
    if not is_valid_email(email):
        errors['email'] = 'Invalid email format.'
    if not is_positive_integer(age):
        errors['age'] = 'Age must be a positive integer.'
    if not is_valid_username(username):
        errors['username'] = 'Username must be 3-20 characters long and can include letters, numbers, and underscores.'
    if not is_valid_password(password):
        errors['password'] = 'Password must be at least 8 characters long, including a number, a letter, and a special character.'
    return errors
