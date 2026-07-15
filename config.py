import json
import os

class ConfigLoader:
    def __init__(self, default_config_path):
        self.default_config_path = default_config_path
        self.config = self.load_defaults()

    def load_defaults(self):
        if not os.path.exists(self.default_config_path):
            raise FileNotFoundError(f"Default config not found at {self.default_config_path}")
        with open(self.default_config_path) as config_file:
            return json.load(config_file)

    def update_config(self, custom_config_path):
        if os.path.exists(custom_config_path):
            with open(custom_config_path) as custom_file:
                custom_config = json.load(custom_file)
            self.config.update(custom_config)

    def get_config(self):
        return self.config

if __name__ == '__main__':
    loader = ConfigLoader('default_config.json')
    loader.update_config('user_config.json')
    print(loader.get_config())