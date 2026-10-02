import os
import json
from typing import Any, Dict

class GameConfig:
    def __init__(self, path: str = 'settings.json'):
        self.path = path
        self.defaults = {
            'fps_limit': 144,
            'render_scale': 1.0,
            'vsync': True,
            'audio_gain': 0.8
        }
        self._data = self._load_or_default()

    def _load_or_default(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            return self.defaults.copy()
        try:
            with open(self.path, 'r') as f:
                loaded = json.load(f)
                return {**self.defaults, **loaded}
        except (json.JSONDecodeError, IOError):
            return self.defaults.copy()

    def __getitem__(self, key: str) -> Any:
        return self._data.get(key, self.defaults.get(key))

    def __getattr__(self, name: str) -> Any:
        if name in self._data:
            return self._data[name]
        raise AttributeError(f'Config key {name} missing')

    def save(self):
        with open(self.path, 'w') as f:
            json.dump(self._data, f, indent=4)

config = GameConfig()