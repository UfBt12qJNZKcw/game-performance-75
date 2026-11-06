import json
import os
from pathlib import Path
from typing import Any, Dict


class PerformanceConfig(dict):
    """Gaming performance configuration loader with hardware-aware defaults."""

    DEFAULTS: Dict[str, Any] = {
        "target_fps": 144,
        "max_render_threads": max(1, (os.cpu_count() or 4) - 1),
        "vsync": False,
        "dynamic_resolution": True,
        "min_scale_factor": 0.65,
        "shader_cache_size_mb": 1024,
        "texture_budget_mb": 4096,
    }

    def __init__(self, config_path: str | Path | None = None):
        super().__init__(self.DEFAULTS)
        self.config_path = Path(config_path) if config_path else None
        self._load_from_disk()
        self._load_env_overrides()

    def _load_from_disk(self) -> None:
        if self.config_path and self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    user_data = json.load(f)
                    if isinstance(user_data, dict):
                        self.update({k: v for k, v in user_data.items() if k in self.DEFAULTS})
            except (json.JSONDecodeError, OSError):
                pass

    def _load_env_overrides(self) -> None:
        prefix = "GAME_PERF_"
        for key, default_val in self.DEFAULTS.items():
            env_key = f"{prefix}{key.upper()}"
            if env_key in os.environ:
                val = os.environ[env_key]
                target_type = type(default_val)
                if target_type is bool:
                    self[key] = val.lower() in ("true", "1", "yes", "on")
                else:
                    try:
                        self[key] = target_type(val)
                    except ValueError:
                        pass

    def __getattr__(self, name: str) -> Any:
        try:
            return self[name]
        except KeyError:
            raise AttributeError(f"No performance parameter named '{name}'")

    def sync_to_disk(self) -> bool:
        if not self.config_path:
            return False
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(dict(self), f, indent=2)
        return True
