import os
import json
from typing import Any, Dict


class PerformanceConfig:
    """A dynamic configuration loader with fallback presets for game-performance-75.

    Supports dictionary merging via the | operator and automatic environment overrides.
    """

    DEFAULT_PRESETS = {
        "target_fps": 60,
        "vsync": True,
        "max_threads": 4,
        "dynamic_resolution": False,
        "shadow_quality": "medium",
        "heap_size_mb": 512,
    }

    def __init__(self, settings: Dict[str, Any] = None):
        self._settings = settings or {}

    def __getattr__(self, name: str) -> Any:
        if name in self._settings:
            val = self._settings[name]
        elif f"GP_{name.upper()}" in os.environ:
            val = os.environ[f"GP_{name.upper()}"]
        elif name in self.DEFAULT_PRESETS:
            val = self.DEFAULT_PRESETS[name]
        else:
            raise AttributeError(f"Configuration key '{name}' not found")

        # Basic type coercion based on default preset types
        default_type = type(self.DEFAULT_PRESETS.get(name, val))
        if default_type is bool and isinstance(val, str):
            return val.lower() in ("true", "1", "yes")
        try:
            return default_type(val)
        except (ValueError, TypeError):
            return val

    def __or__(self, other: "PerformanceConfig") -> "PerformanceConfig":
        """Merge two configurations using the union operator."""
        if not isinstance(other, PerformanceConfig):
            return NotImplemented
        merged = {**self._settings, **other._settings}
        return PerformanceConfig(merged)

    @classmethod
    def load_from_json(cls, filepath: str) -> "PerformanceConfig":
        """Loads configuration from a JSON file, ignoring missing files gracefully."""
        if not os.path.exists(filepath):
            return cls()
        with open(filepath, "r") as f:
            try:
                return cls(json.load(f))
            except json.JSONDecodeError:
                return cls()

    def dump(self) -> Dict[str, Any]:
        """Resolves and dumps the current active state of all configuration parameters."""
        resolved = {}
        for key in self.DEFAULT_PRESETS:
            resolved[key] = getattr(self, key)
        for key in self._settings:
            if key not in resolved:
                resolved[key] = getattr(self, key)
        return resolved
