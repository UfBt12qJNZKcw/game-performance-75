import json
import os

class ConfigurationLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = self.load_config()

    def load_config(self):
        config_path = 'config.json'
        if not os.path.exists(config_path):
            return self.default_config
        with open(config_path, 'r') as config_file:
            return self.merge_configs(self.default_config, json.load(config_file))

    def merge_configs(self, default, user_config):
        for key, value in default.items():
            if key not in user_config:
                user_config[key] = value
        return user_config

# Example usage
if __name__ == '__main__':
    default_config = {'resolution': '1920x1080', 'fullscreen': True, 'volume': 75}
    config_loader = ConfigurationLoader(default_config)
    print(config_loader.config)