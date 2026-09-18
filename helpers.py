import time
import functools
import random

def jitter_backoff(max_retries=3, base_delay=0.5, backoff_factor=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            delay = base_delay
            while retries <= max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    if retries > max_retries:
                        raise e
                    
                    sleep_time = delay * (backoff_factor ** (retries - 1))
                    jitter = sleep_time * 0.1 * random.uniform(-1, 1)
                    time.sleep(sleep_time + jitter)
            return None
        return wrapper
    return decorator

def network_op_wrapper(operation_func):
    """
    Wraps volatile network calls with exponential backoff 
    to stabilize frame-time sensitive game connections.
    """
    @jitter_backoff(max_retries=5, base_delay=0.2)
    def managed_call(*args, **kwargs):
        return operation_func(*args, **kwargs)
    return managed_call