import random
import logging

logging.basicConfig(level=logging.ERROR)

def get_random_item(items):
    try:
        if not items:
            raise ValueError('The items list cannot be empty.')
        return random.choice(items)
    except TypeError:
        logging.error('Provided items is not a list.')
        return None
    except ValueError as ve:
        logging.error(ve)
        return None


def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ZeroDivisionError('Denominator cannot be zero.')
        return numerator / denominator
    except TypeError:
        logging.error('Both numerator and denominator must be numbers.')
        return None
    except ZeroDivisionError as zde:
        logging.error(zde)
        return None


def fetch_user_score(user_id, scores_dict):
    try:
        if user_id not in scores_dict:
            raise KeyError(f'User ID {user_id} not found in scores.')
        return scores_dict[user_id]
    except TypeError:
        logging.error('User ID must be a string or integer.')
        return None
    except KeyError as ke:
        logging.error(ke)
        return None
