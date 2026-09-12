import os
import logging
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, path: str = 'settings.ini'):
        self.path = path
        self._defaults = {'fps_cap': 60, 'vsync': True, 'texture_quality': 'high'}

    def fetch(self, key: str) -> Any:
        try:
            if not os.path.exists(self.path):
                raise FileNotFoundError(f'Config missing at {self.path}')
            with open(self.path, 'r') as f:
                data = {line.split('=')[0].strip(): line.split('=')[1].strip() for line in f if '=' in line}
                return data.get(key, self._defaults.get(key))
        except (OSError, ValueError, IndexError) as e:
            logging.warning(f'Config access failure for {key}: {e}. Returning fallback.')
            return self._defaults.get(key)

    def batch_load(self) -> Dict[str, Any]:
        try:
            if not os.path.isfile(self.path):
                return self._defaults
            with open(self.path, 'r') as f:
                raw = [line.split('=') for line in f if '=' in line]
                return {**self._defaults, **{k.strip(): v.strip() for k, v in raw}}
        except Exception as e:
            logging.critical(f'Catastrophic config parse failure: {e}')
            return self._defaults

def get_instance() -> ConfigLoader:
    return ConfigLoader()