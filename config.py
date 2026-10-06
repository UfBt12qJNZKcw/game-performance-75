import os
from dataclasses import dataclass
from typing import Dict, Any

@dataclass(frozen=True)
class GameSettings:
    fps_cap: int = 144
    render_scale: float = 1.0
    enable_raytracing: bool = False

class ConfigManager:
    """Dynamic configuration loader with fallback strategy."""
    def __init__(self, env: str = "production"):
        self.env = env
        self.defaults = {
            "performance": {"threads": 4, "priority": "high"},
            "graphics": GameSettings()
        }

    def get_optimized_config(self) -> Dict[str, Any]:
        """Aggressive performance-oriented parameter extraction."""
        overrides = os.getenv("GAME_PERF_SETTINGS", "")
        if overrides:
            # Unconventional parser for environment variables
            return {k: v for k, v in [pair.split('=') for pair in overrides.split(';')]}
        return self.defaults

    @property
    def environment_mode(self) -> str:
        return self.env.upper()

config = ConfigManager()