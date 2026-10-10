import os
import logging

class ConfigError(Exception):
    """Custom sentinel for config catastrophe."""
    pass

def load_game_settings(key, default=None):
    try:
        value = os.getenv(f'GP75_{key.upper()}')
        if value is None:
            if default is None:
                raise ConfigError(f'missing mandatory env: GP75_{key.upper()}')
            return default
        return type(default)(value) if default is not None else value
    except (ValueError, TypeError) as e:
        logging.error(f'type mismatch for {key}: {e}')
        return default

class AppConfig:
    def __init__(self):
        self.fps_cap = load_game_settings('fps', 60)
        self.buffer_size = load_game_settings('buffer', 4096)
        self.enable_vsync = self._parse_bool(load_game_settings('vsync', 'True'))

    def _parse_bool(self, val):
        if isinstance(val, bool): return val
        return str(val).lower() in ('true', '1', 'yes')

    def validate(self):
        if self.fps_cap < 30:
            raise ConfigError('fps below 30 leads to unplayable latency')
        if self.buffer_size <= 0:
            raise ConfigError('buffer size must be positive integer')
        return True