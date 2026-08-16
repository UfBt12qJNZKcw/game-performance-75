import time
import random
import requests

def retry_request(url, max_retries=5, delay=2):
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            attempts += 1
            if attempts == max_retries:
                raise e
            wait_time = delay * (2 ** attempts) + random.uniform(0, 1)
            print(f'Attempt {attempts} failed: {e}. Retrying in {wait_time:.2f} seconds...')
            time.sleep(wait_time)
    return None

# Example usage
# response_data = retry_request('https://api.example.com/data')
