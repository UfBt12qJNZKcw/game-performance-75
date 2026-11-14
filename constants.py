from typing import Final, Dict, Tuple

# Configuration constants for game-performance-75 engine

MAX_FRAME_BUFFER: Final[int] = 144
MIN_LATENCY_THRESHOLD_MS: Final[float] = 16.67
DEFAULT_ASSET_PATH: Final[str] = "./assets/v1/"

ENGINE_MODES: Final[Dict[str, int]] = {
    "PERFORMANCE": 0,
    "BALANCED": 1,
    "QUALITY": 2
}

RESOLUTION_PRESETS: Final[Tuple[Tuple[int, int], ...]] = (
    (1280, 720),
    (1920, 1080),
    (2560, 1440),
    (3840, 2160)
)

def get_render_scale(quality_mode: str) -> float:
    """
    Calculate render scale multiplier based on quality profile.

    Args:
        quality_mode: The engine mode key string.

    Returns:
        float: Scaling factor for resolution buffers.
    """
    scales: Dict[str, float] = {
        "PERFORMANCE": 0.75,
        "BALANCED": 1.0,
        "QUALITY": 1.5
    }
    return scales.get(quality_mode, 1.0)

# Bitmask constants for engine features
FEATURE_RAY_TRACING: Final[int] = 1 << 0
FEATURE_DLSS: Final[int] = 1 << 1
FEATURE_V_SYNC: Final[int] = 1 << 2

ENABLED_FEATURES: Final[int] = FEATURE_DLSS | FEATURE_V_SYNC