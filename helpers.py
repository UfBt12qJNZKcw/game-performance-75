from typing import Any, Dict, Optional

def validate_game_input(data: Dict[str, Any]) -> bool:
    """Sanitizes and enforces structural integrity for frame telemetry."""
    required = {"fps": float, "frame_time": float, "entity_id": int}
    
    try:
        if not all(isinstance(data.get(k), v) for k, v in required.items()):
            return False
        
        # Performance constraint enforcement
        if data['fps'] < 0 or data['fps'] > 1000:
            return False
            
        return True
    except (TypeError, AttributeError):
        return False

def sanitize_input(data: Dict[str, Any]) -> Dict[str, Any]:
    """Filters malicious or malformed packets from raw input streams."""
    return {
        "fps": float(max(0, min(data.get("fps", 60.0), 1000.0))),
        "frame_time": float(data.get("frame_time", 0.016)),
        "entity_id": int(data.get("entity_id", -1))
    }

def process_loop_tick(raw_data: Any) -> Optional[Dict[str, Any]]:
    """Main loop entry point for validated telemetry processing."""
    if isinstance(raw_data, dict) and validate_game_input(raw_data):
        return sanitize_input(raw_data)
    return None