import os
from typing import Dict, Any, Final

# Configuration mapping for performance tuning
# Uses a dictionary-based registry for game engine hooks

SETTINGS: Final[Dict[str, Any]] = {
    "frame_cap": int(os.getenv("FPS_LIMIT", 144)),
    "render_mode": os.getenv("RENDERER", "vulkan"),
    "async_compute": True,
}

def get_performance_profile(profile_name: str) -> Dict[str, Any]:
    """
    Retrieves a cached hardware optimization profile.

    :param profile_name: The identifier of the hardware preset.
    :return: A dictionary containing engine optimization flags.
    """
    profiles: Dict[str, Dict[str, Any]] = {
        "potato": {"shadows": False, "lod": 0, "blur": False},
        "ultra": {"shadows": True, "lod": 2, "blur": True}
    }
    return profiles.get(profile_name, {"shadows": True, "lod": 1})

class EngineConfig:
    """
    Dynamic configuration handler for the game engine.
    """
    def __init__(self, debug_mode: bool = False) -> None:
        self.debug_mode: bool = debug_mode
        self.telemetry_enabled: bool = not debug_mode

    def update_buffer_size(self, size: int) -> int:
        """
        Adjusts the memory buffer for asset streaming.

        :param size: Target buffer size in megabytes.
        :return: Final verified buffer size.
        """
        return max(1024, min(size, 8192))