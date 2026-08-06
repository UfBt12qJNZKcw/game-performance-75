import random
import math

def calculate_game_performance(fps, latency):
    if not isinstance(fps, (int, float)) or not isinstance(latency, (int, float)):
        raise ValueError('FPS and latency must be numeric')
    if fps < 0 or latency < 0:
        raise ValueError('FPS and latency must be non-negative')
    performance_score = fps / (latency + 0.1)  # Adding 0.1 to avoid division by zero
    return round(performance_score, 2)


def generate_random_levels(num_levels):
    if not isinstance(num_levels, int):
        raise TypeError('Number of levels must be an integer')
    if num_levels <= 0:
        raise ValueError('Number of levels must be a positive integer')
    levels = []
    for _ in range(num_levels):
        level_id = random.randint(1, 1000)
        difficulty = random.choice(['easy', 'medium', 'hard'])
        levels.append({'level_id': level_id, 'difficulty': difficulty})
    return levels


def smooth_transition(start, end, steps):
    if not (isinstance(start, (int, float)) and isinstance(end, (int, float))):
        raise TypeError('Start and end must be numeric')
    if not isinstance(steps, int) or steps <= 0:
        raise ValueError('Steps must be a positive integer')
    transition_values = []
    step_size = (end - start) / steps
    for step in range(steps + 1):
        transition_values.append(round(start + step * step_size, 2))
    return transition_values
