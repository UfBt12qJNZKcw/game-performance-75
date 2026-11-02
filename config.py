import json
import os
from collections import ChainMap
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "target_fps": 144,
    "resolution_scale": 1.0,
    "max_threads": 8,
    "v_sync": False,
    "preset": "esports",
    "shadow_quality": "medium",
    "telemetry_enabled": True,
    "cache_size_mb": 1024,
}

PRESETS: Dict[str, Dict[str, Any]] = {
    "potato": {"target_fps": 60, "resolution_scale": 0.75, "shadow_quality": "low", "cache_size_mb": 256},
    "esports": {"target_fps": 240, "resolution_scale": 1.0, "shadow_quality": "low", "cache_size_mb": 2048},
    "ultra": {"target_fps": 60, "resolution_scale": 1.0, "shadow_quality": "ultra", "cache_size_mb": 4096},
}

class LazyConfigOverlay:
    """Dynamic configuration layer merging env vars, file overrides, presets, and defaults."""
    def __init__(self, config_path: str = "game_perf.json"):
        self._path = Path(config_path)
        self._file_data = self._load_file()
        self._env_data = self._load_env()
        self._rebuild()

    def _load_file(self) -> Dict[str, Any]:
        if self._path.exists():
            try:
                return json.loads(self._path.read_text())
            except Exception:
                return {}
        return {}

    def _load_env(self) -> Dict[str, Any]:
        env_map = {}
        prefix = "GAME_PERF_"
        for key, val in os.environ.items():
            if key.startswith(prefix):
                clean_key = key[len(prefix):].lower()
                if val.isdigit():
                    env_map[clean_key] = int(val)
                elif val.lower() in ("true", "false"):
                    env_map[clean_key] = val.lower() == "true"
                else:
                    env_map[clean_key] = val
        return env_map

    def _rebuild(self):
        preset_name = self._env_data.get(
            "preset",
            self._file_data.get("preset", DEFAULT_CONFIG["preset"])
        )
        preset_data = PRESETS.get(preset_name, {})
        self._chain = ChainMap(self._env_data, self._file_data, preset_data, DEFAULT_CONFIG)

    def __getattr__(self, name: str) -> Any:
        if name in self._chain:
            return self._chain[name]
        raise AttributeError(f"Configuration key '{name}' does not exist.")

    def __getitem__(self, item: str) -> Any:
        return getattr(self, item)

    def to_dict(self) -> Dict[str, Any]:
        return dict(self._chain)

config = LazyConfigOverlay()
