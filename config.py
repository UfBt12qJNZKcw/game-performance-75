import json

class ConfigLoader:
    DEFAULTS = {
        'screen_resolution': '1920x1080',
        'fullscreen': False,
        'volume': 75,
        'language': 'en'
    }

    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.DEFAULTS.copy()
        self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, 'r') as f:
                user_config = json.load(f)
                self.config.update(user_config)
        except FileNotFoundError:
            print(f'Specified config file {self.config_file} not found, using defaults.')
        except json.JSONDecodeError:
            print('Error reading the config file, using defaults.')

    def get(self, key):
        return self.config.get(key, None)

    def set(self, key, value):
        self.config[key] = value

    def save(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

# Example usage:
# config_loader = ConfigLoader('config.json')
# print(config_loader.get('volume'))
