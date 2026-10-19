import time
import random
import functools
from typing import Callable, Any

def backoff_retry(max_attempts: int = 3, base_delay: float = 0.5):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_ex = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_ex = e
                    sleep_time = base_delay * (2 ** attempt) + random.uniform(0, 0.1)
                    time.sleep(sleep_time)
            raise last_ex or RuntimeError("Failed after retries")
        return wrapper
    return decorator

@backoff_retry(max_attempts=4)
def fetch_game_data(endpoint: str):
    # Simulate volatile network environment for game services
    if random.random() < 0.7:
        raise ConnectionError("Packet loss detected on game server")
    return {"status": "synced", "latency": "low"}

if __name__ == "__main__":
    try:
        data = fetch_game_data("https://api.game-performance-75.net/sync")
        print(f"Payload received: {data}")
    except Exception as e:
        print(f"Critical network failure: {e}")