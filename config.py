import json
import os

class ConfigLoader:
    def __init__(self, default_config_file='default_config.json', user_config_file='user_config.json'):
        self.default_config = self.load_config(default_config_file)
        self.user_config = self.load_config(user_config_file)
        self.final_config = self.merge_configs(self.default_config, self.user_config)

    def load_config(self, filename):
        if not os.path.exists(filename):
            return {}
        with open(filename, 'r') as file:
            return json.load(file)

    def merge_configs(self, default, user):
        config = default.copy()  # Start with the defaults
        config.update(user)      # Override with user settings
        return config

    def get_config(self):
        return self.final_config

# Example usage:
# loader = ConfigLoader()
# print(loader.get_config())
