import random
import math

def roll_dice(sides=6, rolls=1):
    return [random.randint(1, sides) for _ in range(rolls)]

def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def generate_random_position(width, height):
    return (random.randint(0, width), random.randint(0, height))

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)

class GameObject:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def move(self, x_offset, y_offset):
        self.position = (clamp(self.position[0] + x_offset, 0, 1920),
                         clamp(self.position[1] + y_offset, 0, 1080))

    def distance_to(self, other):
        return calculate_distance(self.position, other.position)
