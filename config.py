import os
from typing import Any, Dict

class Settings:
    DEFAULTS = {
        "frame_rate_cap": 144,
        "resolution": (1920, 1080),
        "texture_quality": "ultra",
        "enable_raytracing": False
    }

    def __init__(self, env_prefix: str = "GAME_"):
        self.data = self.DEFAULTS.copy()
        self._load_from_env(env_prefix)

    def _load_from_env(self, prefix: str) -> None:
        for key in self.data:
            env_key = f"{prefix}{key.upper()}"
            val = os.getenv(env_key)
            if val is not None:
                try:
                    self.data[key] = type(self.data[key])(val)
                except (ValueError, TypeError):
                    pass

    def __getattr__(self, name: str) -> Any:
        if name in self.data:
            return self.data[name]
        raise AttributeError(f"config has no attribute {name}")

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

    def __repr__(self) -> str:
        return f"<Config(items={len(self.data)})>"

config = Settings()