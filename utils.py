import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, delay=2, backoff=2):
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            if attempt == retries - 1:
                raise NetworkError(f'Failed to fetch {url} after {retries} attempts') from e
            wait_time = delay * (backoff ** attempt)
            print(f'Attempt {attempt + 1} failed: {e}. Retrying in {wait_time} seconds...')
            time.sleep(wait_time)
            attempt += 1
    return None
