from typing import Dict, Any, Final
from dataclasses import dataclass

@dataclass(frozen=True)
class GameConfig:
    """Immutable storage for global performance parameters."""
    target_fps: int
    resolution: tuple[int, int]
    is_debug: bool

def get_performance_profiles() -> Dict[str, GameConfig]:
    """Generates optimized presets for various hardware tiers."""
    return {
        "ultra": GameConfig(144, (3840, 2160), False),
        "competitive": GameConfig(240, (1920, 1080), True),
        "potato": GameConfig(60, (1280, 720), False)
    }

def validate_setting(key: str, value: Any) -> bool:
    """Sanity check for configuration values."""
    bounds: Dict[str, tuple[int, int]] = {"fov": (60, 120), "volume": (0, 100)}
    if key in bounds:
        low, high = bounds[key]
        return low <= value <= high
    return True

GLOBAL_TIMEOUT: Final[float] = 0.016
"""Target frame time in seconds for 60fps locking."""