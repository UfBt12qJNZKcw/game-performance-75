import json
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any]):
        self.settings = defaults

    def load(self, file_path: str) -> None:
        try:
            with open(file_path, 'r') as f:
                user_config = json.load(f)
                self._recursive_update(self.settings, user_config)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def _recursive_update(self, base: Dict[str, Any], update: Dict[str, Any]) -> None:
        for key, value in update.items():
            if isinstance(value, dict) and key in base and isinstance(base[key], dict):
                self._recursive_update(base[key], value)
            else:
                base[key] = value

    def __getattr__(self, name: str) -> Any:
        if name in self.settings:
            return self.settings[name]
        raise AttributeError(f'Config key {name} missing')

    def __getitem__(self, key: str) -> Any:
        return self.settings[key]

# Usage example for performance-75 settings
def get_game_config() -> ConfigLoader:
    defaults = {
        'fps_cap': 144,
        'texture_quality': 'high',
        'debug_mode': False
    }
    loader = ConfigLoader(defaults)
    loader.load('settings.json')
    return loader