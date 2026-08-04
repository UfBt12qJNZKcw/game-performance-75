import time
import random

class NetworkError(Exception):
    pass

def retry_network_operation(operation, retries=3, delay=2):
    for attempt in range(retries):
        try:
            result = operation()
            return result
        except NetworkError as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay * (1 + random.random()))  # Exponential backoff
            else:
                print(f"All {retries} attempts failed.")
                raise

# Example placeholder for an actual network operation

def sample_network_operation():
    if random.random() < 0.7:  # Simulate a 70% chance of failure
        raise NetworkError("Simulated network failure")
    return "Network operation successful!"

if __name__ == '__main__':
    try:
        result = retry_network_operation(sample_network_operation)
        print(result)
    except NetworkError:
        print("Failed after multiple attempts.")