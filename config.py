import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, user_config_path):
        self.default_config_path = default_config_path
        self.user_config_path = user_config_path
        self.config = self.load_config()

    def load_config(self):
        default_config = self.load_json(self.default_config_path)
        user_config = self.load_json(self.user_config_path) if os.path.exists(self.user_config_path) else {}
        return {**default_config, **user_config}

    def load_json(self, path):
        with open(path, 'r') as f:
            return json.load(f)

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage:
# loader = ConfigLoader('default_config.json', 'user_config.json')
# some_value = loader.get('some_key', 'default_value')