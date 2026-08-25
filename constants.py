from typing import Any, Callable, Dict, List
FPS_ERROR_CODE = 1001
DIVISION_ERROR_CODE = 1002
PLAYER_COUNT_ERROR_CODE = 1003
FRAME_TIME_ERROR_CODE = 1004
DEFAULT_FPS = 60
MIN_FPS_THRESHOLD = 1
MAX_LATENCY_MS = 500
MIN_PLAYERS = 1
MAX_PLAYERS = 128
ERROR_HANDLERS: Dict[int, Callable[[Any], Any]] = {}
def register_handler(code: int, handler: Callable[[Any], Any]) -> None:
    ERROR_HANDLERS[code] = handler
def _handle_negative_fps(value: float) -> float:
    try:
        return float(abs(value)) if value < MIN_FPS_THRESHOLD else float(value)
    except Exception:
        return float(DEFAULT_FPS)
register_handler(FPS_ERROR_CODE, _handle_negative_fps)
def _handle_division_by_zero(value: float) -> float:
    try:
        return float(value) if value != 0 else float(DEFAULT_FPS)
    except Exception:
        return float(DEFAULT_FPS)
register_handler(DIVISION_ERROR_CODE, _handle_division_by_zero)
def _handle_invalid_player_count(count: int) -> int:
    try:
        if count < MIN_PLAYERS: return MIN_PLAYERS
        if count > MAX_PLAYERS: return MAX_PLAYERS
        return count
    except (TypeError, ValueError):
        return MIN_PLAYERS
register_handler(PLAYER_COUNT_ERROR_CODE, _handle_invalid_player_count)
def _handle_frame_time_overflow(time_ms: float) -> float:
    try:
        if time_ms > MAX_LATENCY_MS: return float(MAX_LATENCY_MS)
        return float(max(time_ms, 0))
    except Exception:
        return float(MAX_LATENCY_MS)
register_handler(FRAME_TIME_ERROR_CODE, _handle_frame_time_overflow)
def handle_edge_case(error_code: int, value: Any) -> Any:
    if error_code not in ERROR_HANDLERS:
        return float(DEFAULT_FPS) if isinstance(value, (int, float)) else value
    try:
        return ERROR_HANDLERS[error_code](value)
    except Exception:
        return float(DEFAULT_FPS) if isinstance(value, (int, float)) else value
def calculate_fps_performance(frame_times: List[float], num_players: int) -> float:
    try:
        safe_players = handle_edge_case(PLAYER_COUNT_ERROR_CODE, num_players)
        if safe_players < 1: safe_players = 1
        if len(frame_times) == 0: return float(DEFAULT_FPS)
        processed = [handle_edge_case(FRAME_TIME_ERROR_CODE, t) for t in frame_times]
        total = sum(processed)
        avg_time = total / len(processed) if total > 0 else 1000.0 / DEFAULT_FPS
        raw_fps = 1000 / avg_time if avg_time > 0 else float(DEFAULT_FPS)
        fps = handle_edge_case(FPS_ERROR_CODE, raw_fps)
        return handle_edge_case(DIVISION_ERROR_CODE, fps)
    except Exception:
        return float(DEFAULT_FPS)