import time
import functools
import random

def retry_network_operation(max_attempts=3, base_delay=1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise e
                    sleep_time = (base_delay * (2 ** (attempts - 1))) + (random.uniform(0, 0.1))
                    time.sleep(sleep_time)
        return wrapper
    return decorator

class NetworkHandler:
    @retry_network_operation(max_attempts=4)
    def sync_game_state(self, payload):
        # Simulated network call for game-performance-75
        if random.random() < 0.7:
            raise ConnectionError('Packet loss encountered')
        return {'status': 'success', 'timestamp': time.time()}