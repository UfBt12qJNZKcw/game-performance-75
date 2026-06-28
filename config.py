import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, user_config_path):
        self.default_config = self.load_config(default_config_path)
        self.user_config = self.load_user_config(user_config_path)
        self.final_config = self.merge_configs()

    def load_config(self, config_path):
        with open(config_path, 'r') as file:
            return json.load(file)

    def load_user_config(self, config_path):
        if os.path.exists(config_path):
            with open(config_path, 'r') as file:
                return json.load(file)
        return {}

    def merge_configs(self):
        # Create a new dict based on defaults
        config = self.default_config.copy()
        # Update with user-specific settings
        config.update(self.user_config)
        return config

    def get(self, key, default=None):
        return self.final_config.get(key, default)

# Usage example:
# config = ConfigLoader('default_config.json', 'user_config.json')
# print(config.get('setting_key', 'default_value'))
