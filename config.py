import json
import os
from typing import Any, Dict

class GameConfig:
    DEFAULT_SETTINGS = {
        "frame_rate": 60,
        "resolution": [1920, 1080],
        "vsync": True,
        "debug_mode": False
    }

    def __init__(self, path: str = "settings.json"):
        self.path = path
        self.settings = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            return self.DEFAULT_SETTINGS
        try:
            with open(self.path, "r") as f:
                loaded = json.load(f)
                return {**self.DEFAULT_SETTINGS, **loaded}
        except (json.JSONDecodeError, IOError):
            return self.DEFAULT_SETTINGS

    def __getitem__(self, key: str) -> Any:
        return self.settings.get(key, self.DEFAULT_SETTINGS.get(key))

    def __getattr__(self, name: str) -> Any:
        if name in self.settings:
            return self.settings[name]
        raise AttributeError(f"Config key '{name}' not found")

    def save(self) -> None:
        with open(self.path, "w") as f:
            json.dump(self.settings, f, indent=4)

settings = GameConfig()