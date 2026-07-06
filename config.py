import os

class Config:
    def __init__(self):
        self.settings = self.load_settings()

    def load_settings(self):
        config_file = os.path.join(os.getcwd(), 'config.json')
        if not os.path.exists(config_file):
            raise FileNotFoundError('Configuration file not found.')
        import json
        with open(config_file, 'r') as file:
            return json.load(file)

    def get_setting(self, key):
        return self.settings.get(key, None)

    def update_setting(self, key, value):
        self.settings[key] = value
        self.save_settings()

    def save_settings(self):
        config_file = os.path.join(os.getcwd(), 'config.json')
        with open(config_file, 'w') as file:
            json.dump(self.settings, file, indent=4)

config = Config()