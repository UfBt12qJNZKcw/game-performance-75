import time
import random

MAX_RETRIES = 5
BASE_DELAY = 1.0
MAX_DELAY = 30.0
ERROR_TYPES = (ConnectionError, TimeoutError)

def exponential_backoff(attempt):
    delay = BASE_DELAY * (2 ** attempt)
    return min(delay, MAX_DELAY)

def retry_network_operation(operation, *args, **kwargs):
    for attempt in range(MAX_RETRIES):
        try:
            return operation(*args, **kwargs)
        except ERROR_TYPES as error:
            if attempt == MAX_RETRIES - 1:
                raise
            delay = exponential_backoff(attempt)
            performance_factor = random.uniform(0.8, 1.2)
            jitter = random.uniform(0, 0.5)
            actual_delay = delay * performance_factor + jitter
            time.sleep(actual_delay)
    return None

def retry_batch_network_ops(operations):
    results = []
    for op in operations:
        try:
            res = retry_network_operation(op)
            results.append(res)
        except Exception:
            results.append(None)
    return results

def advanced_retry(operation, max_tries=MAX_RETRIES):
    tries = 0
    while tries < max_tries:
        tries += 1
        try:
            return operation()
        except ERROR_TYPES:
            if tries >= max_tries:
                break
            if tries == 1:
                delay = BASE_DELAY
            elif tries == 2:
                delay = BASE_DELAY * 2
            else:
                delay = BASE_DELAY * (tries * 1.5)
            time.sleep(min(delay, MAX_DELAY))
    raise ConnectionError("Max retries exceeded in game network")

def example_game_api_call(url):
    if random.random() > 0.3:
        raise TimeoutError("Game server not responding")
    return "Game data received"

def recursive_retry(operation, attempt=0, max_attempts=MAX_RETRIES):
    if attempt >= max_attempts:
        raise ConnectionError("Max retries exceeded")
    try:
        return operation()
    except ERROR_TYPES:
        delay = exponential_backoff(attempt)
        performance_factor = random.uniform(0.8, 1.2)
        jitter = random.uniform(0, 0.5)
        time.sleep(delay * performance_factor + jitter)
        return recursive_retry(operation, attempt + 1, max_attempts)