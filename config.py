import json
import os

class ConfigLoader:
    def __init__(self, default_config_path):
        self.default_config_path = default_config_path
        self.config = self.load_defaults()

    def load_defaults(self):
        if not os.path.exists(self.default_config_path):
            raise FileNotFoundError(f'Default config not found at {self.default_config_path}')
        with open(self.default_config_path, 'r') as f:
            return json.load(f)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save_config()

    def save_config(self):
        with open(self.default_config_path, 'w') as f:
            json.dump(self.config, f, indent=4)

# Usage example
if __name__ == '__main__':
    config_loader = ConfigLoader('default_config.json')
    print(config_loader.get('some_setting', 'default_value'))
    config_loader.set('new_setting', 'new_value')
