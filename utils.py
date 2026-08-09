import random
import math


def generate_random_position(x_range, y_range):
    return (random.randint(0, x_range), random.randint(0, y_range))


def calculate_distance(pos1, pos2):
    return math.sqrt((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2)


def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


def lerp(start, end, t):
    return start + (end - start) * t


def normalize_vector(vector):
    length = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
    return (vector[0] / length, vector[1] / length) if length > 0 else (0, 0)


def random_choice_from_list(items):
    return random.choice(items)


def shuffle_list(items):
    random.shuffle(items)
    return items