import time
import random
import requests

def retry_on_failure(max_retries, wait_time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.RequestException as e:
                    print(f'Attempt {retries + 1} failed: {e}')
                    retries += 1
                    if retries < max_retries:
                        sleep_time = wait_time + random.uniform(0, 1)
                        print(f'Retrying in {sleep_time:.2f} seconds...')
                        time.sleep(sleep_time)
            raise Exception('Max retries exceeded')
        return wrapper
    return decorator

@retry_on_failure(max_retries=3, wait_time=2)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    try:
        data = fetch_data(url)
        print(data)
    except Exception as ex:
        print(f'Failed to fetch data: {ex}')