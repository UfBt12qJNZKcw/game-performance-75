import json
import os
from typing import Any, Dict

class GameConfig:
    def __init__(self, filepath: str = 'settings.json', defaults: Dict[str, Any] = None):
        self.filepath = filepath
        self.defaults = defaults or {}
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.filepath):
            return self.defaults.copy()
        with open(self.filepath, 'r') as f:
            try:
                loaded = json.load(f)
                return {**self.defaults, **loaded}
            except json.JSONDecodeError:
                return self.defaults.copy()

    def get(self, key: str, fallback: Any = None) -> Any:
        return self.data.get(key, fallback)

    def save(self) -> None:
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f, indent=4)

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.data[key] = value

def load_performance_settings() -> GameConfig:
    defaults = {
        "fps_limit": 144,
        "resolution": [1920, 1080],
        "vsync": True,
        "shadow_quality": "medium"
    }
    return GameConfig("game_settings.json", defaults)