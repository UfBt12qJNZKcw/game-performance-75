import time
import random
from functools import wraps

def retry_operation(max_retries=3, delay=1, backoff=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    attempt += 1
                    time.sleep(delay)
                    delay *= backoff
            raise Exception(f"All {max_retries} attempts failed")
        return wrapper
    return decorator

@retry_operation(max_retries=5, delay=2)
def network_operation():
    if random.random() < 0.7:
        raise Exception("Network error occurred")
    return "Network request successful" 

if __name__ == '__main__':
    try:
        result = network_operation()
        print(result)
    except Exception as e:
        print(e)