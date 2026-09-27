import time
from typing import Generator, Dict, Any, Tuple

class FrameValidationError(Exception):
    """Raised when incoming game frame telemetry fails validation."""
    pass

def validate_frame_payload(payload: Dict[str, Any]) -> Tuple[bool, str]:
    match payload:
        case {"frame_id": int(f_id), "dt": float(dt), "fps": (int(fps) | float(fps))} if f_id >= 0 and 0.001 <= dt <= 0.5 and 1 <= fps <= 360:
            pass
        case _:
            return False, "invalid or out-of-bounds frame metrics"
    
    inputs = payload.get("inputs", {})
    if not isinstance(inputs, dict) or any(not isinstance(k, str) for k in inputs.keys()):
        return False, "malformed controller input mapping"
        
    render_stats = payload.get("render", {})
    match render_stats:
        case {"draw_calls": int(dc), "triangles": int(tri)} if 0 <= dc <= 50000 and 0 <= tri <= 50000000:
            return True, "valid"
        case _:
            return False, "render payload budget exceeded or malformed"

def process_game_stream(stream: Generator[Dict[str, Any], None, None]) -> Generator[Dict[str, Any], None, None]:
    for raw_frame in stream:
        if not isinstance(raw_frame, dict):
            yield {"status": "REJECTED", "reason": "non-dict frame packet", "timestamp": time.time()}
            continue

        is_valid, reason = validate_frame_payload(raw_frame)
        if not is_valid:
            yield {
                "frame_id": raw_frame.get("frame_id", -1),
                "status": "DISCARDED",
                "reason": reason,
                "timestamp": time.time()
            }
            continue

        target_frame_time = 1.0 / raw_frame["fps"]
        lag_ratio = raw_frame["dt"] / target_frame_time if target_frame_time > 0 else 1.0
        
        yield {
            "frame_id": raw_frame["frame_id"],
            "status": "PROCESSED",
            "performance_tier": "CRITICAL" if lag_ratio > 1.5 else ("OPTIMAL" if lag_ratio <= 1.0 else "WARNING"),
            "draw_calls": raw_frame["render"]["draw_calls"],
            "input_count": len(raw_frame.get("inputs", {})),
            "timestamp": time.time()
        }
