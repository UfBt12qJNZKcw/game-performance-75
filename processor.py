import time
import random
from functools import wraps

def retry_network_call(max_attempts=3, backoff=0.5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise e
                    sleep_time = backoff * (2 ** (attempts - 1)) + random.uniform(0, 0.1)
                    time.sleep(sleep_time)
            return None
        return wrapper
    return decorator

class NetworkProcessor:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    @retry_network_call(max_attempts=4, backoff=1.0)
    def fetch_game_data(self, request_id):
        # Simulate unstable network response
        if random.random() < 0.7:
            raise ConnectionError(f'Latency spike at {self.endpoint}')
        return {'status': 'success', 'id': request_id, 'data': 'payload'}

if __name__ == '__main__':
    proc = NetworkProcessor('https://api.game-perf.75')
    result = proc.fetch_game_data(101)
    print(f'Processed: {result}')