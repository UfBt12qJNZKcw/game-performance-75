import time
import random
import requests

def retry_request(url, retries=5, delay=2):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Assume we want JSON response
        except requests.exceptions.RequestException as e:
            print(f'Attempt {attempt + 1} failed: {e}')
            time.sleep(delay)
            delay *= 2  # Exponential backoff
    return {'error': 'Maximum retries exceeded'}

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = retry_request(url)
    print(data)  # Output the received data
