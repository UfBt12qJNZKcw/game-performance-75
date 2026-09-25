import time
import functools
import random

class NetworkError(Exception):
    pass

def retry_operation(retries=3, delay=1.0, backoff=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except NetworkError as e:
                    if attempt == retries - 1:
                        raise e
                    time.sleep(current_delay + random.uniform(0, 0.1))
                    current_delay *= backoff
        return wrapper
    return decorator

class ConnectionHandler:
    @staticmethod
    @retry_operation(retries=5, delay=0.5)
    def fetch_game_data(endpoint):
        # Simulated network state for game performance monitoring
        if random.random() < 0.7:
            raise NetworkError(f"Latency spike at {endpoint}")
        return {"status": "ready", "payload": [120, 144, 240]}
