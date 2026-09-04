import json
from pathlib import Path
from typing import Any, Dict

class GameConfig:
    DEFAULT_SETTINGS = {
        "fps_limit": 144,
        "vsync": True,
        "resolution": [1920, 1080],
        "graphics_preset": "ultra"
    }

    def __init__(self, config_path: str = "settings.json"):
        self.path = Path(config_path)
        self.data = self._load_or_default()

    def _load_or_default(self) -> Dict[str, Any]:
        if not self.path.exists():
            return self.DEFAULT_SETTINGS.copy()
        try:
            with open(self.path, 'r') as f:
                return {**self.DEFAULT_SETTINGS, **json.load(f)}
        except (json.JSONDecodeError, OSError):
            return self.DEFAULT_SETTINGS.copy()

    def __getitem__(self, key: str) -> Any:
        return self.data.get(key)

    def save(self) -> None:
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)

    def update(self, new_settings: Dict[str, Any]) -> None:
        self.data.update(new_settings)
        self.save()

config = GameConfig()