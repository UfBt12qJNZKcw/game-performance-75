import time
import random
import requests

def retry_request(url, max_retries=5, backoff_factor=1):
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.json()  # Assuming we want JSON response
        except requests.exceptions.RequestException as e:
            attempt += 1
            wait_time = backoff_factor * (2 ** (attempt - 1)) + random.uniform(0, 1)
            print(f'Retry {attempt}/{max_retries} for {url} due to {str(e)}. Waiting {wait_time:.2f} seconds.')
            time.sleep(wait_time)
            if attempt == max_retries:
                raise  # Re-raise the last exception after max retries

# Example usage
if __name__ == '__main__':
    try:
        result = retry_request('https://api.example.com/data')
        print('Success:', result)
    except Exception as final_exception:
        print('Failed after retries:', final_exception)