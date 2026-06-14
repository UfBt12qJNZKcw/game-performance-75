import json
import os

DEFAULT_CONFIG = {
    'resolution': '1920x1080',
    'fullscreen': True,
    'volume': 50,
    'controls': {
        'up': 'w',
        'down': 's',
        'left': 'a',
        'right': 'd',
        'shoot': 'space'
    }
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = DEFAULT_CONFIG.copy()
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                user_config = json.load(f)
                self.config.update(user_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def save(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

# Example usage
if __name__ == '__main__':
    config_loader = ConfigLoader()
    print(config_loader.config)
    config_loader.save()