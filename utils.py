from typing import List, Dict, Any


def calculate_average_score(scores: List[int]) -> float:
    """
    Calculate the average score from a list of scores.

    :param scores: A list of integer scores.
    :return: The average score as a float.
    """
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def filter_high_scores(scores: List[int], threshold: int) -> List[int]:
    """
    Filter the scores to return only those above a certain threshold.

    :param scores: A list of integer scores.
    :param threshold: An integer threshold.
    :return: A list of scores above the threshold.
    """
    return [score for score in scores if score > threshold]


def format_game_data(data: Dict[str, Any]) -> str:
    """
    Format game data for display purposes.

    :param data: A dictionary containing game data like title, genre, and rating.
    :return: A formatted string of the game data.
    """
    title = data.get('title', 'Unknown Game')
    genre = data.get('genre', 'Unknown Genre')
    rating = data.get('rating', 'N/A')
    return f'{title} | Genre: {genre} | Rating: {rating}'
