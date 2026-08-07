import math
import random

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def random_choice(choices):
    return random.choice(choices)


def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


def interpolate(start, end, t):
    return start + (end - start) * t


def debounce(fn, delay):
    last_call = [0]
    def debounced(*args, **kwargs):
        current_time = time.time()
        if current_time - last_call[0] >= delay:
            last_call[0] = current_time
            return fn(*args, **kwargs)
    return debounced


def lerp(start, end, fraction):
    return start + (end - start) * fraction


def ping_pong(value, min_val, max_val):
    if value < min_val or value > max_val:
        return min_val + max_val - value
    return value


def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) if max_val > min_val else 0.0
