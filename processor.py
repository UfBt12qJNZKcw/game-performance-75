from typing import List, Dict, Any


def process_game_data(game_data: List[Dict[str, Any]]) -> Dict[str, float]:
    """Process game performance data.

    Args:
        game_data (List[Dict[str, Any]]): List of game performance metrics.

    Returns:
        Dict[str, float]: Average metrics including FPS and latency.
    """
    total_fps = 0
    total_latency = 0.0
    count = len(game_data)

    for metric in game_data:
        total_fps += metric.get('fps', 0)
        total_latency += metric.get('latency', 0.0)

    avg_fps = total_fps / count if count > 0 else 0
    avg_latency = total_latency / count if count > 0 else 0.0

    return {'average_fps': avg_fps, 'average_latency': avg_latency}


def filter_top_performers(game_data: List[Dict[str, Any]], threshold: float) -> List[Dict[str, Any]]:
    """Filter games that exceed a specified FPS threshold.

    Args:
        game_data (List[Dict[str, Any]]): List of game performance metrics.
        threshold (float): Minimum FPS requirement to be a top performer.

    Returns:
        List[Dict[str, Any]]: Filtered list of top performing games.
    """
    return [game for game in game_data if game.get('fps', 0) > threshold]