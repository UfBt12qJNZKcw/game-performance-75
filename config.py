import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, path: str = 'settings.json', defaults: Dict[str, Any] = None):
        self.path = path
        self.defaults = defaults or {}
        self.data = self._initialize_config()

    def _initialize_config(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            with open(self.path, 'w') as f:
                json.dump(self.defaults, f, indent=4)
            return self.defaults
        
        with open(self.path, 'r') as f:
            try:
                user_data = json.load(f)
                return {**self.defaults, **user_data}
            except json.JSONDecodeError:
                return self.defaults

    def __getitem__(self, key: str) -> Any:
        return self.data.get(key)

    def __getattr__(self, item: str) -> Any:
        return self.data.get(item)

def get_game_config():
    defaults = {
        'fps_cap': 144,
        'vsync': True,
        'render_scale': 1.0,
        'debug_mode': False
    }
    return ConfigLoader('game-performance-75.json', defaults)