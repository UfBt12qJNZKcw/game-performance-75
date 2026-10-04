import time
import functools
import random
import logging

logger = logging.getLogger('game-performance-75')

def retry_network_op(retries=3, backoff=0.5, exceptions=(ConnectionError, TimeoutError)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt == retries:
                        logger.error(f'Critical network failure after {retries} attempts')
                        raise e
                    
                    sleep_time = backoff * (2 ** (attempt - 1)) + random.uniform(0, 0.1)
                    logger.warning(f'Retry {attempt}/{retries} for {func.__name__} after {sleep_time:.2f}s')
                    time.sleep(sleep_time)
        return wrapper
    return decorator

def network_session(endpoint: str):
    @retry_network_op(retries=5, backoff=1.0)
    def fetch_data():
        # Simulated gaming API call
        if random.random() < 0.7:
            raise ConnectionError('Packet loss encountered')
        return {'status': 'success', 'ping': '24ms'}
    return fetch_data()