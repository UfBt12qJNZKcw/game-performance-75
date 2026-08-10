import random
import time
import requests

def retry_request(url, max_retries=5, delay=2):
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Attempt {attempt + 1} failed: {e}')
            attempt += 1
            if attempt < max_retries:
                wait_time = delay * (2 ** (attempt - 1))  # Exponential backoff
                print(f'Waiting for {wait_time} seconds before retrying...')
                time.sleep(wait_time)
    raise Exception(f'Max retries exceeded for URL: {url}')

# Example usage:
if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry_request(url)
        print('Data retrieved:', data)
    except Exception as e:
        print('Failed to retrieve data:', e)