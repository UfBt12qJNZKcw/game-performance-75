import random
import math

def generate_random_position(x_range, y_range):
    """
    Generate a random position.
    Returns a tuple of (x, y).
    """
    x = random.randint(0, x_range)
    y = random.randint(0, y_range)
    return (x, y)


def distance(point1, point2):
    """
    Calculate the Euclidean distance between two points.
    point1 and point2 are tuples of (x, y).
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def clamp(value, min_value, max_value):
    """
    Clamp a value between min_value and max_value.
    """
    return max(min_value, min(value, max_value))


def lerp(start, end, fraction):
    """
    Linearly interpolate between start and end by fraction.
    """
    return start + (end - start) * fraction


def normalize(vector):
    """
    Normalize a vector (x, y).
    """
    length = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
    if length == 0:
        return (0, 0)
    return (vector[0] / length, vector[1] / length)