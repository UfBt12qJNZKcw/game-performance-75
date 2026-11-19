import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, path: str = "config.json", defaults: Dict[str, Any] = None):
        self.path = path
        self.defaults = defaults or {}

    def load(self) -> Dict[str, Any]:
        try:
            if os.path.exists(self.path):
                with open(self.path, 'r') as f:
                    data = json.load(f)
                return {**self.defaults, **data}
            return self.defaults
        except (json.JSONDecodeError, IOError):
            return self.defaults

    def __getitem__(self, key: str) -> Any:
        return self.load().get(key)

def get_game_config(overrides: Dict[str, Any] = None) -> Dict[str, Any]:
    base = {
        "fps_cap": 144,
        "vsync": True,
        "resolution": [1920, 1080],
        "graphics_preset": "ultra"
    }
    loader = ConfigLoader("settings.json", base)
    config = loader.load()
    if overrides:
        config.update(overrides)
    return config

if __name__ == "__main__":
    cfg = get_game_config({"fps_cap": 240})
    print(f"Active performance config: {cfg}")