import random
import time

def get_random_element(sequence):
    """Returns a random element from a non-empty sequence."""
    if not sequence:
        raise ValueError('Cannot get random element from an empty sequence')
    return random.choice(sequence)


def measure_execution_time(func):
    """Decorator to measure execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Execution time: {end_time - start_time:.4f} seconds')
        return result
    return wrapper


def clamp(value, min_value, max_value):
    """Clamps a value between a minimum and maximum value."""
    return max(min(value, max_value), min_value)


def interpolate(start, end, fraction):
    """Linearly interpolates between start and end based on fraction."""
    return start + (end - start) * fraction


def shuffle_list(original_list):
    """Returns a shuffled copy of the original list."""
    shuffled = original_list[:]
    random.shuffle(shuffled)
    return shuffled
