import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, path: str = 'settings.json', defaults: Dict[str, Any] = None):
        self.path = path
        self.data = defaults or {}
        self.load()

    def load(self) -> None:
        if os.path.exists(self.path):
            try:
                with open(self.path, 'r') as f:
                    self.data.update(json.load(f))
            except (json.JSONDecodeError, IOError):
                pass

    def __getitem__(self, key: str) -> Any:
        return self.data.get(key)

    def __getattr__(self, name: str) -> Any:
        return self.data.get(name)

def get_config(path: str = 'settings.json') -> ConfigLoader:
    defaults = {
        'fps_cap': 60,
        'vsync': True,
        'render_scale': 1.0,
        'debug_mode': False
    }
    return ConfigLoader(path, defaults)

# Dynamic attribute access for game engine configs
settings = get_config()