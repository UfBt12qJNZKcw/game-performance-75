import time
import functools
import random
import logging

logger = logging.getLogger('game-performance-75')

class NetworkRetryError(Exception):
    """Exception raised when retries are exhausted."""
    pass

def retry_operation(max_attempts=3, backoff_factor=0.5):
    """
    decorator applying jittered exponential backoff to network functions.
    unconventional approach: uses a closure to maintain state during failures.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f'operation {func.__name__} failed after {attempts} attempts')
                        raise NetworkRetryError(f'exhausted {max_attempts} retries') from e
                    
                    sleep_time = (backoff_factor * (2 ** attempts)) + (random.random() * 0.1)
                    logger.warning(f'retry {attempts}/{max_attempts} for {func.__name__} in {sleep_time:.2f}s')
                    time.sleep(sleep_time)
        return wrapper
    return decorator