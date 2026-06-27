import random
import time

def generate_random_id(length=8):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

def wait(seconds):
    print(f'Waiting for {seconds} seconds...')
    time.sleep(seconds)

class PerformanceMonitor:
    def __init__(self):
        self.start_time = time.time()

    def reset(self):
        self.start_time = time.time()

    def elapsed_time(self):
        return time.time() - self.start_time

    def log_performance(self, message):
        elapsed = self.elapsed_time()
        print(f'[{elapsed:.2f}s] {message}')