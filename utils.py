from typing import List, Union


def calculate_average(scores: List[Union[int, float]]) -> float:
    """
    Calculate the average of a list of scores.
    
    Parameters:
    scores (List[Union[int, float]]): A list of scores to average.
    
    Returns:
    float: The average of the scores.
    """
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def find_highest_score(scores: List[Union[int, float]]) -> Union[int, float, None]:
    """
    Find the highest score in a list of scores.
    
    Parameters:
    scores (List[Union[int, float]]): A list of scores.
    
    Returns:
    Union[int, float, None]: The highest score or None if the list is empty.
    """
    if not scores:
        return None
    return max(scores)


def is_score_valid(score: Union[int, float]) -> bool:
    """
    Check if a score is valid (non-negative).
    
    Parameters:
    score (Union[int, float]): The score to validate.
    
    Returns:
    bool: True if the score is valid, False otherwise.
    """
    return isinstance(score, (int, float)) and score >= 0


def get_pass_fail(average: float, passing_score: float = 60.0) -> str:
    """
    Determine if the average score is a pass or fail.
    
    Parameters:
    average (float): The average score.
    passing_score (float): The score required to pass (default is 60.0).
    
    Returns:
    str: 'Pass' if the average is greater than or equal to the passing score, 'Fail' otherwise.
    """
    return 'Pass' if average >= passing_score else 'Fail'