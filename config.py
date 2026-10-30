import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Dynamic configuration loader with fallback strategy."""
    DEFAULTS = {
        "fps_cap": 144,
        "vsync": True,
        "render_scale": 1.0,
        "debug_mode": False
    }

    def __init__(self, config_path: str = "settings.json"):
        self.path = config_path
        self.data = self.DEFAULTS.copy()
        self._load()

    def _load(self) -> None:
        if os.path.exists(self.path):
            try:
                with open(self.path, "r") as f:
                    loaded = json.load(f)
                    self.data.update({k: v for k, v in loaded.items() if k in self.DEFAULTS})
            except (json.JSONDecodeError, IOError):
                pass

    def __getattr__(self, name: str) -> Any:
        return self.data.get(name, self.DEFAULTS.get(name))

    def save(self) -> None:
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=4)

    def update(self, **kwargs) -> None:
        self.data.update({k: v for k, v in kwargs.items() if k in self.DEFAULTS})
        self.save()