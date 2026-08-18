import random
import math


def generate_random_position(bounds):
    x = random.randint(bounds['x_min'], bounds['x_max'])
    y = random.randint(bounds['y_min'], bounds['y_max'])
    return (x, y)


def calculate_distance(point_a, point_b):
    return math.sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2)


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def interpolate(start, end, t):
    return start + (end - start) * t


def choose_random_item(items):
    return random.choice(items)


def shuffle_list(items):
    random.shuffle(items)
    return items


def print_vector(vector):
    print(f'Vector: x={vector[0]}, y={vector[1]}')