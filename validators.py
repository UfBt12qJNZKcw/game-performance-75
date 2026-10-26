import time
import functools
from typing import Callable, Any, Type

def retry_network_call(retries: int = 3, delay: float = 1.0, backoff: int = 2):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            local_delay = delay
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    if attempt < retries - 1:
                        time.sleep(local_delay)
                        local_delay *= backoff
            raise last_exception
        return wrapper
    return decorator

class ConnectionValidator:
    def __init__(self, target_node: str):
        self.target = target_node

    @retry_network_call(retries=5, delay=0.5)
    def validate_connection(self) -> bool:
        # Simulate unstable network in game-performance-75 context
        import random
        if random.random() < 0.7:
            raise ConnectionError(f"Latency spike detected on {self.target}")
        return True