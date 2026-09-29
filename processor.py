import json
import os
from typing import Any, Dict

class ConfigProcessor:
    def __init__(self, defaults: Dict[str, Any], path: str = 'settings.json'):
        self.path = path
        self.config = defaults
        self._load_and_merge()

    def _load_and_merge(self) -> None:
        if not os.path.exists(self.path):
            return
        try:
            with open(self.path, 'r') as f:
                user_data = json.load(f)
                self._recursive_update(self.config, user_data)
        except (json.JSONDecodeError, IOError):
            pass

    def _recursive_update(self, base: Dict, patch: Dict) -> None:
        for key, value in patch.items():
            if isinstance(value, dict) and key in base and isinstance(base[key], dict):
                self._recursive_update(base[key], value)
            else:
                base[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.config[key]

    def __repr__(self) -> str:
        return f"ConfigProcessor({self.config})"