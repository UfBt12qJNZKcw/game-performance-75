import json
import os
from dataclasses import dataclass, field, fields
from typing import Any, Dict, get_type_hints


@dataclass
class GameConfig:
    target_fps: int = 144
    render_scale: float = 1.0
    v_sync: bool = False
    thread_budget: int = 8
    cache_dir: str = ".cache/textures"
    flags: dict = field(default_factory=lambda: {"async_compute": True, "hdr": False})

    def __getitem__(self, key: str) -> Any:
        return getattr(self, key)

    def __or__(self, other: Dict[str, Any]) -> "GameConfig":
        merged = {}
        type_map = get_type_hints(self.__class__)
        for f in fields(self):
            val = other.get(f.name, getattr(self, f.name))
            expected_type = type_map.get(f.name, type(val))
            if isinstance(val, str) and expected_type is bool:
                val = val.lower() in ("true", "1", "yes", "on")
            elif not isinstance(val, expected_type) and expected_type in (int, float, str):
                try:
                    val = expected_type(val)
                except (ValueError, TypeError):
                    val = getattr(self, f.name)
            merged[f.name] = val
        return GameConfig(**merged)


class ConfigLoader:
    @staticmethod
    def load(file_path: str = "settings.json", env_prefix: str = "GAME_PERF_") -> GameConfig:
        config = GameConfig()
        file_overrides = {}
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    file_overrides = json.load(f)
            except (json.JSONDecodeError, OSError):
                file_overrides = {}

        env_overrides = {}
        for key, val in os.environ.items():
            if key.startswith(env_prefix):
                clean_key = key[len(env_prefix):].lower()
                env_overrides[clean_key] = val

        return config | file_overrides | env_overrides
