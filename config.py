import json
import os

class ConfigLoader:
    def __init__(self, default_config_file='default_config.json', user_config_file='user_config.json'):
        self.default_config = self.load_config(default_config_file)
        self.user_config = self.load_config(user_config_file)
        self.config = self.merge_configs(self.default_config, self.user_config)

    def load_config(self, filename):
        if not os.path.exists(filename):
            return {}
        with open(filename, 'r') as file:
            return json.load(file)

    def merge_configs(self, default, user):
        merged = default.copy()
        merged.update(user)
        return merged

    def get(self, key, default_value=None):
        return self.config.get(key, default_value)

if __name__ == '__main__':
    config_loader = ConfigLoader()
    print(config_loader.config)  
