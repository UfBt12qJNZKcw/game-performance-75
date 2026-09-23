import time
import functools
import random
import logging

logger = logging.getLogger('game-performance-75')

def retry_network_op(retries=3, backoff=0.5, jitter=True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= retries:
                        logger.error(f'operation failed after {attempts} attempts')
                        raise
                    sleep_time = backoff * (2 ** (attempts - 1))
                    if jitter:
                        sleep_time += random.uniform(0, 0.1 * sleep_time)
                    logger.warning(f'retry {attempts}/{retries} due to {e}')
                    time.sleep(sleep_time)
        return wrapper
    return decorator

@retry_network_op(retries=5)
def fetch_server_metrics(endpoint):
    # simulated network interaction for game performance tracking
    logger.info(f'querying {endpoint}')
    return {'fps': 144, 'latency': 20}