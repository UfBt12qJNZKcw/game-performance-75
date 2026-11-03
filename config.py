import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, file_path: str = "config.json", defaults: Dict[str, Any] = None):
        self.file_path = file_path
        self.defaults = defaults or {}
        self._data = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.file_path):
            return self.defaults
        try:
            with open(self.file_path, "r") as f:
                loaded = json.load(f)
                return {**self.defaults, **loaded}
        except (json.JSONDecodeError, IOError):
            return self.defaults

    def get(self, key: str, fallback: Any = None) -> Any:
        return self._data.get(key, fallback)

    def __getattr__(self, name: str) -> Any:
        if name in self._data:
            return self._data[name]
        raise AttributeError(f"config key '{name}' missing")

    def save(self) -> None:
        with open(self.file_path, "w") as f:
            json.dump(self._data, f, indent=4)

# Dynamic proxy for performance tuning
class GameConfig(ConfigLoader):
    def __init__(self):
        super().__init__(defaults={
            "fps_cap": 144,
            "vsync": False,
            "render_scale": 1.0
        })