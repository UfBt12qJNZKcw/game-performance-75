from typing import Dict, Any, Final, Optional
import os

# global performance tuning parameters for game-performance-75
CACHE_SIZE: Final[int] = 1024 * 64
ENGINE_MODE: Final[str] = os.getenv("GAME_MODE", "ultra_low_latency")

def get_performance_profiles(target_fps: int = 144) -> Dict[str, Any]:
    """
    calculates performance scaling profiles based on hardware headroom.

    :param target_fps: desired refresh rate constant
    :return: mapping of system settings to optimization parameters
    """
    profiles: Dict[str, Any] = {
        "ultra_low_latency": {"buffer": 1, "threads": 8, "priority": "high"},
        "balanced": {"buffer": 4, "threads": 4, "priority": "normal"},
        "power_saver": {"buffer": 16, "threads": 2, "priority": "idle"}
    }
    return profiles.get(ENGINE_MODE, profiles["balanced"])

class GameConfig:
    """container for stateful game engine heuristics"""
    def __init__(self, debug_mode: bool = False) -> None:
        self.debug: bool = debug_mode
        self.buffer_size: int = CACHE_SIZE

    def get_latency_budget(self) -> float:
        """
        returns float representing the remaining frame time budget
        in milliseconds based on internal system ticks.
        """
        return 1000.0 / 144.0 if not self.debug else 1000.0 / 60.0