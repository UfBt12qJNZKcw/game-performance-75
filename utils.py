import time
import random
import requests

def retry_request(url, max_retries=5, backoff_factor=0.3):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            retries += 1
            wait_time = backoff_factor * (2 ** retries)
            print(f'Attempt {retries} failed: {e}. Retrying in {wait_time:.1f} seconds...')
            time.sleep(wait_time)
    raise Exception('Max retries exceeded')

# Example usage (uncomment to test):
# result = retry_request('https://api.example.com/data')
# print(result)