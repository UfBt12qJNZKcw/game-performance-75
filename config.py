import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Dynamic configuration mapper with nested default injection."""
    def __init__(self, defaults: Dict[str, Any]):
        self._data = defaults

    def load(self, path: str) -> None:
        if not os.path.exists(path):
            return
        with open(path, 'r') as f:
            user_config = json.load(f)
            self._deep_merge(self._data, user_config)

    def _deep_merge(self, base: Dict, patch: Dict) -> None:
        for key, value in patch.items():
            if isinstance(value, dict) and key in base and isinstance(base[key], dict):
                self._deep_merge(base[key], value)
            else:
                base[key] = value

    def get(self, key_path: str, default: Any = None) -> Any:
        keys = key_path.split('.')
        curr = self._data
        try:
            for k in keys:
                curr = curr[k]
            return curr
        except (KeyError, TypeError):
            return default

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

def create_config(path: str, defaults: Dict[str, Any]) -> ConfigLoader:
    loader = ConfigLoader(defaults)
    loader.load(path)
    return loader