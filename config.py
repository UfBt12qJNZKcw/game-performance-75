import json
import os

class ConfigLoader:
    def __init__(self, default_config_path):
        self.default_config_path = default_config_path
        self.config = self.load_defaults()

    def load_defaults(self):
        if not os.path.exists(self.default_config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.default_config_path}")
        with open(self.default_config_path, 'r') as file:
            return json.load(file)

    def get(self, key, fallback=None):
        return self.config.get(key, fallback)

    def update(self, new_config):
        self.config.update(new_config)

if __name__ == '__main__':
    loader = ConfigLoader('default_config.json')
    print(loader.get('game_resolution', '1920x1080'))
    loader.update({'game_resolution': '2560x1440'})
    print(loader.get('game_resolution'))