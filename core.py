import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any], path: str = 'settings.json'):
        self.path = path
        self.data = defaults
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        if os.path.exists(self.path):
            try:
                with open(self.path, 'r') as f:
                    loaded = json.load(f)
                    self.data.update({k: v for k, v in loaded.items() if k in self.data})
            except (json.JSONDecodeError, IOError):
                pass

    def __getitem__(self, key: str) -> Any:
        return self.data.get(key)

    def persist(self) -> None:
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)

    def patch(self, updates: Dict[str, Any]) -> None:
        self.data.update(updates)
        self.persist()

    def __repr__(self) -> str:
        return f"<GameConfig current={len(self.data)} entries>"

# Usage example for performance-critical pathing
def get_game_config():
    defaults = {"fps_cap": 60, "vsync": True, "render_scale": 1.0}
    return ConfigLoader(defaults)