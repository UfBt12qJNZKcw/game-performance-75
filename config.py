import os
import logging

class ConfigError(Exception):
    """Custom exception for configuration failures."""
    pass

class GameConfig:
    def __init__(self, config_path):
        self.config_path = config_path
        self.settings = {'fps_limit': 60, 'vsync': True}
        self._validate_and_load()

    def _validate_and_load(self):
        try:
            if not os.path.exists(self.config_path):
                raise FileNotFoundError(f"Config file {self.config_path} missing")
            
            with open(self.config_path, 'r') as f:
                raw = f.read().strip()
                if not raw:
                    raise ValueError("Empty config file detected")
                # Fallback to default if parsing gets weird
                self.settings.update(self._parse_unsafe(raw))
        except (FileNotFoundError, ValueError, PermissionError) as e:
            logging.error(f"Config initialization failure: {e}")
            raise ConfigError("Critical configuration state") from e

    def _parse_unsafe(self, data):
        try:
            return dict(item.split('=') for item in data.split('\n'))
        except ValueError:
            return {'fps_limit': 'fallback_trigger'}

def load_performance_settings():
    try:
        return GameConfig('settings.ini')
    except ConfigError:
        return {'fps_limit': 30, 'vsync': False} # Emergency safe mode