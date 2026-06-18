import json
import os

class ConfigLoader:
    def __init__(self, default_config_file, custom_config_file=None):
        self.default_config_file = default_config_file
        self.custom_config_file = custom_config_file
        self.config = self.load_config()

    def load_config(self):
        defaults = self.load_json(self.default_config_file)
        custom = self.load_json(self.custom_config_file) if self.custom_config_file else {}
        return {**defaults, **custom}

    def load_json(self, filename):
        if not os.path.exists(filename):
            return {}
        with open(filename, 'r') as file:
            return json.load(file)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def __repr__(self):
        return json.dumps(self.config, indent=4)

# Example usage (not required for functionality)
# if __name__ == '__main__':
#     config_loader = ConfigLoader('default_config.json', 'custom_config.json')
#     print(config_loader)