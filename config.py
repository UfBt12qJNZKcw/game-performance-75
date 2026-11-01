import json
import math
import os
from typing import Any, Dict, Union

DEFAULT_GAMING_PROFILE: Dict[str, Union[int, float, str, bool]] = {
    "target_fps": 60,
    "max_frame_latency_ms": 16.67,
    "resolution_scale": 1.0,
    "dynamic_resolution": True,
    "v_sync": False,
    "gpu_power_limit_watts": 250,
}


class EdgeCaseSafeConfig:
    """Creative game config loader with dynamic healing for extreme edge cases."""

    def __init__(self, config_path: str = "game_settings.json") -> None:
        self.config_path = config_path
        self._data: Dict[str, Any] = {}
        self.reload()

    def reload(self) -> None:
        raw_data = self._read_raw_file()
        self._data = {
            key: self._sanitize_setting(key, raw_data.get(key, default))
            for key, default in DEFAULT_GAMING_PROFILE.items()
        }

    def _read_raw_file(self) -> Dict[str, Any]:
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    return json.loads(content) if content else {}
        except (json.JSONDecodeError, OSError, PermissionError):
            pass
        return {}

    def _sanitize_setting(self, key: str, value: Any) -> Union[int, float, str, bool]:
        try:
            if key == "target_fps":
                val = int(value)
                return max(15, min(val, 360)) if val > 0 else 60
            elif key == "resolution_scale":
                val = float(value)
                if math.isnan(val) or math.isinf(val):
                    return 1.0
                return max(0.25, min(val, 2.0))
            elif key == "max_frame_latency_ms":
                val = float(value)
                return 16.67 if (math.isnan(val) or val <= 0) else min(val, 1000.0)
            elif key == "gpu_power_limit_watts":
                val = int(value)
                return max(50, min(val, 600))
            elif isinstance(DEFAULT_GAMING_PROFILE.get(key), bool):
                return bool(value)
        except (ValueError, TypeError):
            pass
        return DEFAULT_GAMING_PROFILE[key]

    def get(self, key: str) -> Any:
        return self._data.get(key, DEFAULT_GAMING_PROFILE.get(key))

    def __getitem__(self, key: str) -> Any:
        return self.get(key)
