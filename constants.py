from typing import Final, Dict, Any
from dataclasses import dataclass

@dataclass(frozen=True)
class PerformanceThresholds:
    FPS_MIN: int = 60
    LATENCY_MAX_MS: int = 50
    FRAME_TIME_MAX_MS: float = 16.6

class GameConstants:
    VERSION: Final[str] = "0.7.5-stable"
    TICK_RATE_HZ: Final[int] = 128
    ENGINE_PRESETS: Final[Dict[str, Any]] = {
        "ULTRA": {"shadows": True, "anti_aliasing": 8, "v_sync": False},
        "COMPETITIVE": {"shadows": False, "anti_aliasing": 0, "v_sync": False},
        "POWER_SAVER": {"shadows": False, "anti_aliasing": 0, "v_sync": True}
    }

def get_preset_config(quality_mode: str) -> Dict[str, Any]:
    """Fetches engine configuration based on performance tier."""
    return GameConstants.ENGINE_PRESETS.get(
        quality_mode.upper(), 
        GameConstants.ENGINE_PRESETS["COMPETITIVE"]
    )

def validate_telemetry(metric_key: str, value: float) -> bool:
    """Checks if metric stays within performance bounds."""
    limits = PerformanceThresholds()
    mapping = {
        "fps": lambda v: v >= limits.FPS_MIN,
        "latency": lambda v: v <= limits.LATENCY_MAX_MS,
        "frame_time": lambda v: v <= limits.FRAME_TIME_MAX_MS
    }
    
    validator = mapping.get(metric_key, lambda _: True)
    return validator(value)