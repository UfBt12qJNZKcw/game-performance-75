import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, path: str = 'settings.json'):
        self.path = path
        self.defaults = {
            'fps_limit': 60,
            'vsync': True,
            'render_scale': 1.0,
            'audio_gain': 0.8
        }

    def load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            self._persist_defaults()
            return self.defaults
        
        with open(self.path, 'r') as f:
            try:
                user_cfg = json.load(f)
            except json.JSONDecodeError:
                return self.defaults
        
        return {**self.defaults, **user_cfg}

    def _persist_defaults(self) -> None:
        try:
            with open(self.path, 'w') as f:
                json.dump(self.defaults, f, indent=4)
        except IOError:
            pass

def get_app_config(key: str = None) -> Any:
    loader = ConfigLoader()
    config = loader.load()
    return config.get(key) if key else config