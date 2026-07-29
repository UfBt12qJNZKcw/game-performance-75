import time
import random
import requests

def retry_request(url, max_retries=5, backoff_factor=1, timeout=5):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            print(f'Timeout occurred. Attempt {retries + 1} of {max_retries}.')
        except requests.exceptions.HTTPError as err:
            print(f'HTTP error occurred: {err}. Attempt {retries + 1} of {max_retries}.')
        except requests.exceptions.RequestException as err:
            print(f'An error occurred: {err}. Attempt {retries + 1} of {max_retries}.')
        retries += 1
        time.sleep(backoff_factor * (2 ** retries))  # Exponential backoff
    raise Exception('Max retries exceeded')

# Example usage
#if __name__ == '__main__':
#    result = retry_request('https://api.example.com/data')
#    print(result)