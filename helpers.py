from typing import List, Dict, Any


def calculate_average(scores: List[float]) -> float:
    """
    Calculate the average of a list of scores.

    Args:
        scores (List[float]): A list of numerical scores.

    Returns:
        float: The average of the provided scores.
    """
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def get_top_players(players: Dict[str, List[float]], top_n: int = 3) -> Dict[str, float]:
    """
    Get the top N players based on their scores.

    Args:
        players (Dict[str, List[float]]): A dictionary with player names as keys and their scores as values.
        top_n (int): The number of top players to return.

    Returns:
        Dict[str, float]: A dictionary of top players and their average scores.
    """
    averages = {player: calculate_average(scores) for player, scores in players.items()}
    top_players = dict(sorted(averages.items(), key=lambda item: item[1], reverse=True)[:top_n])
    return top_players


def format_scoreboard(players: Dict[str, float]) -> str:
    """
    Format the scoreboard for display.

    Args:
        players (Dict[str, float]): A dictionary of player names and their scores.

    Returns:
        str: A formatted scoreboard.
    """
    return '\n'.join([f'{player}: {score:.2f}' for player, score in players.items()])
