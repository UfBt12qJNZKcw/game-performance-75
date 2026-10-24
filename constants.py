from typing import Final, Dict, Tuple

# Frame-budget settings for the engine core
FPS_TARGET: Final[int] = 144
FRAME_TIME_MS: Final[float] = 1000.0 / FPS_TARGET

# Graphics presets mapping for dynamic adjustment
PRESETS: Final[Dict[str, float]] = {
    "low": 0.5,
    "medium": 1.0,
    "high": 1.5,
    "ultra": 2.0
}

# Hardware buffer constraints
MAX_BUFFER_SIZE: Final[int] = 1024 * 64

# Color palette for diagnostic overlays
COLORS: Final[Dict[str, Tuple[int, int, int]]] = {
    "fps_good": (0, 255, 0),
    "fps_warn": (255, 255, 0),
    "fps_crit": (255, 0, 0)
}

def get_buffer_limit(multiplier: float = 1.0) -> int:
    """Calculates the memory cap for rendering buffers based on hardware scaling."""
    return int(MAX_BUFFER_SIZE * multiplier)

# Global session flag
SESSION_ID: Final[str] = "game-performance-75-dev"

# Engine state constants
ENGINE_STATES: Final[Tuple[str, ...]] = ("INIT", "LOADING", "RUNNING", "HALTED")