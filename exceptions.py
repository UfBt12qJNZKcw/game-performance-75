import time
import functools
import logging

logger = logging.getLogger('game-performance-75')

class NetworkRetryException(Exception):
    pass

def with_retry(retries=3, delay=1.5, backoff=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            current_delay = delay
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError, NetworkRetryException) as e:
                    attempt += 1
                    if attempt >= retries:
                        logger.critical(f"failed after {retries} attempts: {e}")
                        raise
                    
                    # Exponential jitter-like wait for game engine stability
                    wait_time = current_delay + (attempt * 0.1)
                    logger.warning(f"retry {attempt}/{retries} in {wait_time:.2f}s")
                    time.sleep(wait_time)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator