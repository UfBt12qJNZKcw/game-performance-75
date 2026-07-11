import time
import random
from functools import wraps


def retry(max_retries=5, delay=2):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return function(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_retries:
                        raise
                    print(f'Attempt {attempts} failed: {e}, retrying in {delay}s...')
                    time.sleep(delay)
                    delay *= 2  # Exponential backoff
        return wrapper
    return decorator


@retry(max_retries=3, delay=1)
def fetch_data_from_network():
    if random.choice([True, False]):
        raise ConnectionError('Network error occurred!')
    return 'Data fetched successfully!'

# Example Usage:
if __name__ == '__main__':
    result = fetch_data_from_network()
    print(result)
