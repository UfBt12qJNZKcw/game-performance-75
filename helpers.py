import time
import random

class NetworkError(Exception):
    pass

def perform_network_operation():
    if random.choice([True, False]):  # Simulate network fluctuation
        raise NetworkError("Network issue occurred")
    return "Success!"


def retry_operation(max_retries=5, delay=2):
    retries = 0
    while retries < max_retries:
        try:
            result = perform_network_operation()
            return result
        except NetworkError as e:
            print(f"Attempt {retries + 1}: {e}")
            retries += 1
            time.sleep(delay)
    return "Failed after max retries"

# Example usage of retry logic:
if __name__ == '__main__':
    result = retry_operation()
    print(result)