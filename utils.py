import random
import time
from typing import List, Any

def shuffle_list(items: List[Any]) -> List[Any]:
    shuffled = items[:]
    random.shuffle(shuffled)
    return shuffled


def sleep_seconds(seconds: float) -> None:
    time.sleep(seconds)


def format_time(milliseconds: int) -> str:
    seconds = milliseconds / 1000
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f'{int(hours):02}:{int(minutes):02}:{int(seconds):02}'


def clamp(value: float, min_value: float, max_value: float) -> float:
    return max(min(value, max_value), min_value)


def average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers) if numbers else 0.0


def get_random_choice(choices: List[Any]) -> Any:
    return random.choice(choices)