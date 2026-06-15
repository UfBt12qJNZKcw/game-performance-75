import json
import os

DEFAULT_CONFIG = {
    'resolution': '1920x1080',
    'volume': 75,
    'fullscreen': True,
    'controls': {
        'move_up': 'W',
        'move_down': 'S',
        'move_left': 'A',
        'move_right': 'D',
        'shoot': 'SPACE'
    }
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                user_config = json.load(file)
                return self.override_defaults(user_config)
        return DEFAULT_CONFIG

    def override_defaults(self, user_config):
        combined_config = DEFAULT_CONFIG.copy()
        combined_config.update(user_config)
        return combined_config

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage:
# config_loader = ConfigLoader()
# print(config_loader.get('volume'))