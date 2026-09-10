import os
import logging
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, path: str = 'settings.cfg'):
        self.path = path
        self.settings: Dict[str, Any] = {'fps_cap': 60, 'vsync': True}

    def load(self) -> Dict[str, Any]:
        try:
            if not os.path.exists(self.path):
                raise FileNotFoundError(f'Config missing at {self.path}')
            with open(self.path, 'r') as f:
                for line in f:
                    key, val = line.strip().split('=')
                    self.settings[key.strip()] = self._cast_value(val.strip())
        except (ValueError, IOError) as e:
            logging.warning(f'Config malformed, using defaults: {e}')
            self.settings = {'fps_cap': 60, 'vsync': True}
        return self.settings

    def _cast_value(self, val: str) -> Any:
        if val.lower() in ('true', 'false'):
            return val.lower() == 'true'
        try:
            return int(val)
        except ValueError:
            return val

def get_app_config() -> Dict[str, Any]:
    loader = ConfigLoader()
    return loader.load()