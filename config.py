import json
import os

class ConfigLoader:
    def __init__(self, default_config_path):
        self.default_config = self.load_default_config(default_config_path)
        self.user_config = {}

    def load_default_config(self, path):
        with open(path, 'r') as file:
            return json.load(file)

    def load_user_config(self, user_config_path):
        if os.path.exists(user_config_path):
            with open(user_config_path, 'r') as file:
                self.user_config = json.load(file)
        else:
            self.user_config = {}

    def get_config(self):
        config = self.default_config.copy()
        config.update(self.user_config)
        return config

# Usage example
if __name__ == '__main__':
    loader = ConfigLoader('default_config.json')
    loader.load_user_config('user_config.json')
    final_config = loader.get_config()
    print(final_config)