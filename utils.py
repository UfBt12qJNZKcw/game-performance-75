import random
import time
from functools import wraps

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f}s")
        return result
    return wrapper


def random_choice(choices):
    if not choices:
        raise ValueError("Choices must not be empty")
    return random.choice(choices)


def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


def normalize_angle(angle):
    while angle < 0:
        angle += 360
    while angle >= 360:
        angle -= 360
    return angle


def calculate_distance(point_a, point_b):
    dx = point_b[0] - point_a[0]
    dy = point_b[1] - point_a[1]
    return (dx ** 2 + dy ** 2) ** 0.5
