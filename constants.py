import math

# Game constants
FPS = 60
PLAYER_SPEED = 5.0
GRAVITY = 9.81
JUMP_HEIGHT = 1.5

# Color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Level constants
MAX_LEVELS = 10
BOSS_HEALTH = 1000

# Utility functions

def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def radians_to_degrees(radians):
    return radians * (180.0 / math.pi)


def degrees_to_radians(degrees):
    return degrees * (math.pi / 180.0)