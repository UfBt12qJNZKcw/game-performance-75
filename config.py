import json
import os

class Config:
    def __init__(self, filename='config.json'):
        self.filename = filename
        self.settings = self.load_config()  

    def load_config(self):
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, 'r') as file:
            return json.load(file)

    def get_setting(self, key, default=None):
        return self.settings.get(key, default)

    def set_setting(self, key, value):
        self.settings[key] = value
        self.save_config()

    def save_config(self):
        with open(self.filename, 'w') as file:
            json.dump(self.settings, file, indent=4)

# Example usage
if __name__ == '__main__':
    config = Config()
    print(config.get_setting('resolution', '1920x1080'))
    config.set_setting('fullscreen', True)