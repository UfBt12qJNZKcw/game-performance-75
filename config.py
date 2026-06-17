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
        return self.merge_configs(default_config, user_config)

    def load_json(self, path):
        with open(path, 'r') as f:
            return json.load(f)

    def merge_configs(self, default, user):
        merged = default.copy()
        merged.update(user)
        return merged

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example of usage:
# config_loader = ConfigLoader('default_config.json', 'user_config.json')
# db_host = config_loader.get('db_host', 'localhost')