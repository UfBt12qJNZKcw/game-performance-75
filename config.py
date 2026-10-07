import json
import os
from typing import Any, Dict

class GameConfig:
    def __init__(self, path: str, defaults: Dict[str, Any]):
        self.path = path
        self.data = defaults.copy()
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        if os.path.exists(self.path):
            try:
                with open(self.path, 'r') as f:
                    disk_data = json.load(f)
                    self.data.update({k: v for k, v in disk_data.items() if k in self.data})
            except (json.JSONDecodeError, IOError):
                pass

    def __getattr__(self, name: str) -> Any:
        return self.data.get(name)

    def __setattr__(self, name: str, value: Any) -> None:
        if name in ['path', 'data']:
            super().__setattr__(name, value)
        else:
            self.data[name] = value

def get_loader(path: str) -> GameConfig:
    defaults = {
        'fps_cap': 60,
        'vsync': True,
        'resolution': (1920, 1080),
        'texture_quality': 'high'
    }
    return GameConfig(path, defaults)