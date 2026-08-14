import json
import os

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.settings = {}
        self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            raise ConfigError(f'Configuration file not found: {self.config_file}')
        try:
            with open(self.config_file, 'r') as file:
                self.settings = json.load(file)
        except json.JSONDecodeError:
            raise ConfigError('Error decoding JSON from configuration file')
        except Exception as e:
            raise ConfigError(f'Unexpected error: {str(e)}')

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value

    def save(self):
        try:
            with open(self.config_file, 'w') as file:
                json.dump(self.settings, file, indent=4)
        except Exception as e:
            raise ConfigError(f'Error saving configuration: {str(e)}')
