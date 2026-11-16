import time
import functools
import logging

logger = logging.getLogger('game-performance-75')

def retry_network_op(retries=3, delay=1.5, backoff=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt, current_delay = 0, delay
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempt += 1
                    if attempt == retries:
                        logger.error(f'Network op failed after {retries} attempts')
                        raise
                    logger.warning(f'Retry {attempt}/{retries} due to {e}')
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_network_op(retries=5, delay=0.5)
def ping_server(addr):
    # Simulate volatile gaming network latency
    import random
    if random.random() < 0.7:
        raise ConnectionError('Packet drop detected')
    return True