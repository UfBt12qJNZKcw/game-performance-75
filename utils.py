import random
import math

def random_position(limit_x, limit_y):
    return (random.randint(0, limit_x), random.randint(0, limit_y))


def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


def lerp(start, end, t):
    return start + (end - start) * t


def choose_random(lst):
    return random.choice(lst)


def normalize_vector(vector):
    length = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
    if length == 0:
        return (0, 0)
    return (vector[0] / length, vector[1] / length)