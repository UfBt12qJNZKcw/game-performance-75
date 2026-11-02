import os
import sys

class ConfigLoader:
    """Handles game config loading with aggressive fallback strategies."""
    def __init__(self, path):
        self.path = path
        self.defaults = {"fps_cap": 60, "vsync": True, "render_scale": 1.0}

    def load_safe(self):
        try:
            if not os.path.exists(self.path):
                raise FileNotFoundError("Config missing, defaulting")
            with open(self.path, 'r') as f:
                return self._parse(f.read())
        except (FileNotFoundError, PermissionError, OSError) as e:
            print(f"[PERF-WARN] fallback to safe config: {e}")
            return self.defaults
        except Exception:
            return self.defaults

    def _parse(self, content):
        data = {}
        for line in content.splitlines():
            if '=' in line:
                k, v = line.split('=', 1)
                try:
                    data[k.strip()] = float(v.strip())
                except ValueError:
                    continue
        return {**self.defaults, **data}

    def validate(self, cfg):
        # Niche constraint: ensure game doesn't crash on absurd values
        for k, v in cfg.items():
            if k == "render_scale" and not (0.1 <= v <= 4.0):
                cfg[k] = 1.0
            if k == "fps_cap" and v < 30:
                cfg[k] = 30
        return cfg

def get_game_config(path="settings.ini"):
    loader = ConfigLoader(path)
    raw = loader.load_safe()
    return loader.validate(raw)