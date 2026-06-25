import time
import random

def retry_with_backoff(max_retries=5, backoff_factor=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    delay = backoff_factor * (2 ** retries) + random.uniform(0, 1)
                    print(f"Error: {e}. Retrying in {delay:.2f} seconds...")
                    time.sleep(delay)
                    retries += 1
            raise Exception(f'Exceeded maximum retries ({max_retries}) for function {func.__name__}')
        return wrapper
    return decorator

@retry_with_backoff()
def fetch_data_from_server():
    if random.random() < 0.7:
        raise ConnectionError("Connection failed")
    return "Data received successfully!"