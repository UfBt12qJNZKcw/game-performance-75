import time
import functools
import random
import logging

logger = logging.getLogger('game-performance-75')

def retry_network_op(max_attempts=3, base_delay=0.5, backoff=2.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = base_delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logger.error(f'Critical network failure after {attempts} attempts')
                        raise e
                    sleep_time = current_delay * (backoff ** (attempts - 1)) + (random.uniform(0, 0.1))
                    logger.warning(f'Network glitch, retrying in {sleep_time:.2f}s (attempt {attempts})')
                    time.sleep(sleep_time)
            return None
        return wrapper
    return decorator

@retry_network_op(max_attempts=4)
def fetch_game_server_data(endpoint):
    # Simulate volatile network connection for game assets
    if random.random() < 0.7:
        raise ConnectionError('Packet loss encountered')
    return {'status': 'active', 'players': 42, 'tickrate': 128.0}