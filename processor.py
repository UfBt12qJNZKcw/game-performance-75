import time
from typing import Dict, Any, Generator, Tuple

class FrameTelemetryError(ValueError):
    """Raised when frame metric telemetry violates runtime safety bounds."""
    pass

def validate_frame_packet(raw_packet: Dict[str, Any]) -> Dict[str, Any]:
    """Validates raw render metrics against dynamic engine safety bounds using bitmasks."""
    required_keys = {"frame_id", "delta_ms", "gpu_temp_c", "draw_calls"}
    if not required_keys.issubset(raw_packet.keys()):
        missing = required_keys - raw_packet.keys()
        raise FrameTelemetryError(f"Malformed telemetry frame missing keys: {missing}")

    frame_id = raw_packet["frame_id"]
    delta_ms = raw_packet["delta_ms"]
    gpu_temp = raw_packet["gpu_temp_c"]
    draw_calls = raw_packet["draw_calls"]

    # Bitwise status mask for out-of-bounds metrics (Delta, Temp, DrawCalls)
    status_flags = 0
    if not (0.1 <= float(delta_ms) <= 1000.0):
        status_flags |= 0b001
    if not (0.0 <= float(gpu_temp) <= 120.0):
        status_flags |= 0b010
    if not (0 <= int(draw_calls) <= 500000):
        status_flags |= 0b100

    if status_flags != 0:
        raise FrameTelemetryError(f"Frame {frame_id} failed validation with mask: 0b{status_flags:03b}")

    return {
        "frame_id": int(frame_id),
        "delta_ms": float(delta_ms),
        "gpu_temp_c": float(gpu_temp),
        "draw_calls": int(draw_calls),
        "fps": 1000.0 / float(delta_ms) if delta_ms > 0 else 0.0
    }

def main_processing_loop(packet_stream: Generator[Dict[str, Any], None, None]) -> Generator[Tuple[bool, Dict[str, Any]], None, None]:
    """Main game telemetry processing loop performing streaming packet validation."""
    for raw_packet in packet_stream:
        try:
            validated = validate_frame_packet(raw_packet)
            yield True, validated
        except (FrameTelemetryError, TypeError, ValueError, KeyError) as err:
            yield False, {"error": str(err), "raw": raw_packet}
