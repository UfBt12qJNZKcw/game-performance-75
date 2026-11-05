from typing import Any, Dict, Optional

def validate_frame_data(data: Any) -> Dict[str, Any]:
    """Sanitizes incoming game telemetry with aggressive type casting."""
    if not isinstance(data, dict):
        raise ValueError("Frame payload must be a dictionary")

    required = {'latency': float, 'fps': int, 'entity_count': int}
    sanitized = {}

    for key, expected_type in required.items():
        value = data.get(key)
        if value is None:
            sanitized[key] = expected_type(0)
        else:
            try:
                sanitized[key] = expected_type(value)
            except (ValueError, TypeError):
                sanitized[key] = expected_type(0)

    # Enforce performance bounds
    sanitized['fps'] = max(0, min(sanitized['fps'], 500))
    sanitized['latency'] = max(0.0, min(sanitized['latency'], 1000.0))
    
    return sanitized

def process_input_stream(stream: Any) -> Optional[Dict[str, Any]]:
    """Main loop entry point for stream validation."""
    try:
        return validate_frame_data(stream)
    except Exception:
        return None