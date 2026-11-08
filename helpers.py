import time
import functools
import random
import logging

logger = logging.getLogger('game-performance-75')

def retry_with_jitter(max_attempts=3, base_delay=1.0):
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
                        logger.error(f'Critical network failure after {attempts} attempts: {e}')
                        raise
                    
                    # Exponential backoff with 50% random jitter
                    delay = (base_delay * (2 ** (attempts - 1))) * (0.5 + 0.5 * random.random())
                    logger.warning(f'Network glitch, retrying in {delay:.2f}s... (attempt {attempts})')
                    time.sleep(delay)
        return wrapper
    return decorator

def network_operation(func):
    """Facade for specialized network retry behavior."""
    return retry_with_jitter(max_attempts=5, base_delay=0.5)(func)