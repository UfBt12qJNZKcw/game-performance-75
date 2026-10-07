import time
import functools
import logging

logger = logging.getLogger('game-performance-75')

class NetworkRetry:
    def __init__(self, retries=3, backoff=0.5):
        self.retries = retries
        self.backoff = backoff

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_ex = None
            for attempt in range(self.retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_ex = e
                    wait = self.backoff * (2 ** attempt)
                    logger.warning(f'Network glitch, retrying in {wait}s...')
                    time.sleep(wait)
            raise last_ex
        return wrapper

class FatalNetworkError(Exception):
    """Raised when retries are exhausted."""
    pass

def retry_operation(retries=3, backoff=0.5):
    return NetworkRetry(retries, backoff)