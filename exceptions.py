import time
import random

class NetworkError(Exception):
    pass

class RetryExceededError(Exception):
    pass

def retry_on_failure(max_retries=5, backoff_factor=1.0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except NetworkError as e:
                    retries += 1
                    sleep_time = backoff_factor * (2 ** retries)
                    print(f'Attempt {retries} failed: {e}, retrying in {sleep_time:.1f}s...')
                    time.sleep(sleep_time)
            raise RetryExceededError(f'Max retries exceeded for {func.__name__}')
        return wrapper
    return decorator

@retry_on_failure(max_retries=3, backoff_factor=0.5)
def unstable_network_request():
    if random.random() < 0.7:
        raise NetworkError('Simulated network failure!')
    return 'Success!'
