import time
import random
from functools import wraps

def retry_operation(max_attempts=3, backoff_factor=1.5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            delay = 1.0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise e
                    sleep_time = delay + random.uniform(0, 0.5)
                    time.sleep(sleep_time)
                    delay *= backoff_factor
        return wrapper
    return decorator

class NetworkProcessor:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    @retry_operation(max_attempts=4)
    def fetch_game_data(self, request_id):
        # Simulate volatile network state
        if random.random() < 0.7:
            raise ConnectionError(f"Latency spike on {self.endpoint}")
        return {"status": "success", "data": "high_score_packet", "id": request_id}

def process_packet(raw_id):
    processor = NetworkProcessor("https://game-perf.local/v1")
    result = processor.fetch_game_data(raw_id)
    return f"Processed: {result['data']}"