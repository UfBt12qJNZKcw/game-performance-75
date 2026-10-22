import json
import os
from pathlib import Path
from typing import Any, Dict

DEFAULT_SETTINGS: Dict[str, Any] = {
    "target_fps": 120,
    "resolution_scale": 1.0,
    "ray_tracing": False,
    "vram_limit_mb": 6144,
    "frame_pacing_sync": "vsync",
}


class DynamicGameConfig:
    """Cascading configuration manager for gaming engine performance presets."""

    def __init__(self, file_path: str = "perf_config.json") -> None:
        self.file_path = Path(file_path)
        self._store: Dict[str, Any] = {}
        self.load()

    def load(self) -> "DynamicGameConfig":
        file_data: Dict[str, Any] = {}
        if self.file_path.is_file():
            try:
                file_data = json.loads(self.file_path.read_text())
            except json.JSONDecodeError:
                file_data = {}

        # Fallback sequence: Default -> File -> Environment variables
        for key, default_val in DEFAULT_SETTINGS.items():
            env_key = f"GAME_PERF_{key.upper()}"
            raw_env = os.environ.get(env_key)

            if raw_env is not None:
                value = self._cast(raw_env, type(default_val))
            else:
                value = file_data.get(key, default_val)

            self._store[key] = value
        return self

    @staticmethod
    def _cast(val: str, target_type: type) -> Any:
        if target_type is bool:
            return val.lower() in ("true", "1", "yes", "on")
        try:
            return target_type(val)
        except (ValueError, TypeError):
            return val

    def __getattr__(self, name: str) -> Any:
        try:
            return self._store[name]
        except KeyError:
            raise AttributeError(f"Invalid performance config key: {name}")

    def __or__(self, override: Dict[str, Any]) -> "DynamicGameConfig":
        """Bitwise OR syntax to produce dynamic live overrides."""
        new_cfg = DynamicGameConfig.__new__(DynamicGameConfig)
        new_cfg.file_path = self.file_path
        new_cfg._store = {**self._store, **override}
        return new_cfg


active_config = DynamicGameConfig()
