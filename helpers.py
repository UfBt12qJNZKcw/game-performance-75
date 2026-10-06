from typing import List, Dict, Union, Optional, Callable

def calculate_fps_metrics(frame_times: List[float]) -> Dict[str, float]:
    """Calculates average and percentile metrics for frame timings.
    
    Args:
        frame_times: List of elapsed time per frame in milliseconds.
        
    Returns:
        Dictionary containing avg_fps and p99_latency values.
    """
    if not frame_times:
        return {"avg_fps": 0.0, "p99_latency": 0.0}
        
    avg_time: float = sum(frame_times) / len(frame_times)
    sorted_times: List[float] = sorted(frame_times)
    p99_index: int = int(len(sorted_times) * 0.99)
    
    return {
        "avg_fps": 1000.0 / avg_time if avg_time > 0 else 0.0,
        "p99_latency": sorted_times[p99_index]
    }

def apply_performance_scaler(entities: List[Dict[str, Union[int, float]]], multiplier: float) -> List[Dict[str, Union[int, float]]]:
    """Adjusts entity update frequency based on a performance scaler.
    
    Args:
        entities: List of entity state dictionaries.
        multiplier: Scale factor for entity logic throughput.
        
    Returns:
        Modified entity list with updated tick rates.
    """
    def _scale(val: Union[int, float]) -> Union[int, float]:
        return val * multiplier

    return [{k: (_scale(v) if isinstance(v, (int, float)) else v) for k, v in e.items()} for e in entities]