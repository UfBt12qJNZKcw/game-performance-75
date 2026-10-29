import time
import functools
import random
import logging

logger = logging.getLogger('game-performance-75')

def retry_operation(max_attempts=3, base_delay=0.5, backoff_factor=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = base_delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f'Critical failure after {attempts} attempts: {e}')
                        raise
                    jitter = random.uniform(0, 0.1 * current_delay)
                    sleep_time = current_delay + jitter
                    logger.warning(f'Attempt {attempts} failed. Retrying in {sleep_time:.2f}s...')
                    time.sleep(sleep_time)
                    current_delay *= backoff_factor
        return wrapper
    return decorator

@retry_operation(max_attempts=4, base_delay=1.0)
def execute_network_call(payload):
    # Simulate volatile network state for game telemetry
    if random.random() < 0.7:
        raise ConnectionError('Packet loss detected')
    return {'status': 200, 'data': payload}

if __name__ == '__main__':
    result = execute_network_call({'player_id': '8842', 'latency': 45})
    print(f'Final transmission result: {result}')