import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, max_retries=5, backoff_factor=1):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            retries += 1
            if retries == max_retries:
                print(f"Max retries exceeded. Error: {e}")
                raise NetworkError(f"Failed to fetch {url}")
            wait_time = backoff_factor * (2 ** (retries - 1))
            print(f"Retrying in {wait_time} seconds...")
            time.sleep(wait_time)

# Example usage:
# data = retry_request('https://api.example.com/data')
# print(data)