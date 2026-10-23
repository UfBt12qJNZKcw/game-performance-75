import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Dynamic attribute-based configuration management for gaming performance."""
    def __init__(self, defaults: Dict[str, Any], path: str = 'settings.json'):
        self._defaults = defaults
        self._path = path
        self._data = defaults.copy()
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        if os.path.exists(self._path):
            try:
                with open(self._path, 'r') as f:
                    self._data.update(json.load(f))
            except (json.JSONDecodeError, IOError):
                pass

    def __getattr__(self, name: str) -> Any:
        return self._data.get(name, self._defaults.get(name))

    def __getitem__(self, key: str) -> Any:
        return self._data.get(key)

def get_game_config() -> ConfigLoader:
    defaults = {
        "fps_limit": 144,
        "vsync": True,
        "texture_quality": "ultra",
        "enable_raytracing": False
    }
    return ConfigLoader(defaults)

config = get_game_config()