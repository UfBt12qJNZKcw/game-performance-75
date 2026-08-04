import time
import random
import requests

class NetworkError(Exception):
    pass

def perform_request(url, retries=3, delay=2):
    for attempt in range(retries):
        try:
            print(f'Attempt {attempt + 1} to reach {url}')
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Error: {e}')
            if attempt < retries - 1:
                wait_time = delay + random.uniform(0, 1)
                print(f'Retrying in {wait_time:.2f} seconds...')
                time.sleep(wait_time)
            else:
                raise NetworkError(f'Failed to reach {url} after {retries} attempts')

if __name__ == '__main__':
    try:
        data = perform_request('https://api.example.com/data')
        print('Data received:', data)
    except NetworkError as e:
        print(e)