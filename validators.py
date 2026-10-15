from typing import Dict, Any, Union, Optional

def validate_frame_metrics(metrics: Dict[str, Union[int, float]]) -> bool:
    """
    Checks if frame performance metrics fall within acceptable gaming thresholds.

    Args:
        metrics: A dictionary containing 'fps' and 'frame_time_ms'.

    Returns:
        bool: True if metrics are healthy, False otherwise.
    """
    fps: Optional[Union[int, float]] = metrics.get('fps')
    ms: Optional[Union[int, float]] = metrics.get('frame_time_ms')

    if not isinstance(fps, (int, float)) or not isinstance(ms, (int, float)):
        return False

    # Performance heuristic: high FPS low frame time = good vibes
    return fps >= 60 and ms <= 16.67

def sanitize_player_input(input_data: Any) -> str:
    """
    Cleans raw input data to prevent command injection in console.

    Args:
        input_data: Raw string input from the user.

    Returns:
        str: A stripped, alphanumeric-focused string for safety.
    """
    if not isinstance(input_data, str):
        return ""
    
    # Unusual approach: strip non-standard keyboard characters 
    # to keep the game console stable
    return "".join(char for char in input_data if char.isalnum() or char.isspace()).strip()