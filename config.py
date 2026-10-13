import json
import os
from pathlib import Path
from typing import Any, Dict

class GameConfig:
    DEFAULT_SETTINGS = {
        "resolution": [1920, 1080],
        "vsync": True,
        "target_fps": 144,
        "shadow_quality": "ultra"
    }

    def __init__(self, config_path: str = "settings.json"):
        self.path = Path(config_path)
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        if not self.path.exists():
            return self.DEFAULT_SETTINGS.copy()
        try:
            with open(self.path, "r") as f:
                user_data = json.load(f)
                return {**self.DEFAULT_SETTINGS, **user_data}
        except (json.JSONDecodeError, OSError):
            return self.DEFAULT_SETTINGS.copy()

    def get(self, key: str, fallback: Any = None) -> Any:
        return self.data.get(key, fallback)

    def save(self) -> None:
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=4)

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

    def __repr__(self) -> str:
        return f"<GameConfig active_settings={len(self.data)}>"