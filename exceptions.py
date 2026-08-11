import time
import random

class NetworkError(Exception):
    pass

class Retry:
    def __init__(self, max_attempts=3, base_delay=1, backoff_factor=2):
        self.max_attempts = max_attempts
        self.base_delay = base_delay
        self.backoff_factor = backoff_factor

    def execute(self, func, *args, **kwargs):
        attempts = 0
        while attempts < self.max_attempts:
            try:
                return func(*args, **kwargs)
            except NetworkError as e:
                attempts += 1
                wait_time = self.base_delay * (self.backoff_factor ** (attempts - 1))
                print(f"Attempt {attempts} failed: {e}. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
        raise NetworkError(f"All {self.max_attempts} attempts failed.")

# Example usage:
def mock_network_operation(success_rate=0.5):
    if random.random() > success_rate:
        raise NetworkError("Network operation failed")
    return "Network operation succeeded"

if __name__ == '__main__':
    retry = Retry(max_attempts=5)
    result = retry.execute(mock_network_operation)
    print(result)