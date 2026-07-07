import time
import random

class NetworkError(Exception):
    pass

def network_operation():
    if random.choice([True, False]):
        raise NetworkError("Simulated network error")
    return "Success"


def retry_decorator(retries=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except NetworkError as e:
                    print(f'Attempt {attempt + 1} failed: {e}')
                    time.sleep(delay)
                    if attempt == retries - 1:
                        print('All retries failed')
                        raise
        return wrapper
    return decorator

@retry_decorator(retries=5, delay=1)
def perform_network_request():
    return network_operation()

if __name__ == '__main__':
    try:
        result = perform_network_request()
        print(result)
    except NetworkError:
        print('Failed to complete network request')
