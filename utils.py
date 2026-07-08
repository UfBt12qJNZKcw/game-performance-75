import time
import random
import requests

def retry_request(url, max_retries=5, backoff_factor=0.3, timeout=10):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.ConnectionError as ce:
            print(f"Connection error: {ce}")
        except requests.Timeout as te:
            print(f"Timeout error: {te}")
        except requests.HTTPError as he:
            print(f"HTTP error: {he}")
            return None
        retries += 1
        wait_time = backoff_factor * (2 ** (retries - 1)) + random.uniform(0, 1)
        print(f"Retrying in {wait_time:.2f} seconds...")
        time.sleep(wait_time)
    return None
