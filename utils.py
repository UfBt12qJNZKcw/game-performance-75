import time
import random

def retry_on_failure(max_retries=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    print(f'Network error: {e}. Retrying... ({retries + 1}/{max_retries})')
                    time.sleep(delay)
                    retries += 1
            print('Max retries reached. Operation failed.')
            return None
        return wrapper
    return decorator

@retry_on_failure(max_retries=5, delay=1)
def simulate_network_operation():
    if random.choice([True, False]):
        raise ConnectionError('Simulated connection failure')
    return 'Success!'

# Example of calling the function
if __name__ == '__main__':
    result = simulate_network_operation()
    print(result)