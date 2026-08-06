from typing import List, Dict


def calculate_fps(frames: List[int], time_duration: float) -> float:
    """
    Calculate frames per second (FPS) based on the number of frames
    captured in a given time duration.

    Args:
        frames (List[int]): A list of frame timestamps in milliseconds.
        time_duration (float): The total duration in seconds during which frames were captured.

    Returns:
        float: The calculated frames per second.
    """
    if time_duration <= 0:
        raise ValueError('Time duration must be greater than zero.')
    return len(frames) / time_duration


def average_ping(pings: List[int]) -> float:
    """
    Calculate the average ping from a list of pings.

    Args:
        pings (List[int]): A list of ping times in milliseconds.

    Returns:
        float: The average ping time.
    """
    if not pings:
        return 0.0
    return sum(pings) / len(pings)


def format_stats(stats: Dict[str, float]) -> str:
    """
    Format game statistics into a readable string.

    Args:
        stats (Dict[str, float]): A dictionary of game statistics.

    Returns:
        str: A formatted string of statistics.
    """
    return '\n'.join(f'{key}: {value:.2f}' for key, value in stats.items())
