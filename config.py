import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, user_config_path):
        self.default_config = self.load_config(default_config_path)
        self.user_config = self.load_config(user_config_path) if os.path.exists(user_config_path) else {}

    def load_config(self, path):
        with open(path, 'r') as config_file:
            return json.load(config_file)

    def get_config(self):
        combined_config = self.default_config.copy()
        combined_config.update(self.user_config)
        return combined_config

if __name__ == '__main__':
    config_loader = ConfigLoader('default_config.json', 'user_config.json')
    config = config_loader.get_config()
    print(config)