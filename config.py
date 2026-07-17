import json
import os

class ConfigLoader:
    def __init__(self, default_config, user_config_path):
        self.default_config = default_config
        self.user_config_path = user_config_path
        self.config = self.load_config()

    def load_config(self):
        config = self.default_config.copy()
        if os.path.exists(self.user_config_path):
            with open(self.user_config_path, 'r') as user_config_file:
                user_config = json.load(user_config_file)
                config.update(user_config)
        return config

    def get(self, key, default=None):
        return self.config.get(key, default)

# Usage example:
if __name__ == '__main__':
    defaults = {'volume': 50, 'resolution': '1920x1080'}
    loader = ConfigLoader(defaults, 'user_config.json')
    print(loader.get('volume'))
    print(loader.get('resolution'))
    print(loader.get('fullscreen', False))
