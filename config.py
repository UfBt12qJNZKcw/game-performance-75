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
            with open(self.path, 'r') as f:
                try:
                    self.data.update(json.load(f))
                except json.JSONDecodeError:
                    pass

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

    def save(self) -> None:
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)

# Dynamic proxy for attribute-based access
def __getattr__(name: str) -> Any:
    loader = ConfigLoader()
    return loader.get(name)
