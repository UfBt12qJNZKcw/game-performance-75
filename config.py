import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = default_config.copy()

    def load_config(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                try:
                    user_config = json.load(file)
                    self.update_config(user_config)
                except json.JSONDecodeError:
                    print('Invalid JSON in config file.')
        else:
            print('Config file not found. Using defaults.')

    def update_config(self, user_config):
        for key, value in user_config.items():
            if key in self.default_config:
                self.config[key] = value

    def get_config(self):
        return self.config

# Example usage:
# default_config = {'setting1': True, 'setting2': 'default'}
# config_loader = ConfigLoader(default_config)
# config_loader.load_config('path/to/config.json')
# print(config_loader.get_config())