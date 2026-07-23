import re

class InputValidator:
    @staticmethod
    def is_valid_username(username):
        return bool(re.match(r'^[a-zA-Z0-9_]{3,16}$', username))

    @staticmethod
    def is_valid_email(email):
        return bool(re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email))

    @staticmethod
    def is_valid_password(password):
        return (len(password) >= 8 and 
                any(c.isdigit() for c in password) and 
                any(c.isupper() for c in password) and 
                any(c.islower() for c in password))

    @staticmethod
    def validate_input(username, email, password):
        if not InputValidator.is_valid_username(username):
            raise ValueError('Invalid username')
        if not InputValidator.is_valid_email(email):
            raise ValueError('Invalid email')
        if not InputValidator.is_valid_password(password):
            raise ValueError('Invalid password')
        return True
