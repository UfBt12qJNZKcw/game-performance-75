import json
import os

DEFAULT_CONFIG = {
    'volume': 50,
    'resolution': '1920x1080',
    'fullscreen': True,
    'language': 'en'
}

def load_config(file_path):
    if not os.path.exists(file_path):
        return DEFAULT_CONFIG
    with open(file_path, 'r') as config_file:
        try:
            user_config = json.load(config_file)
        except json.JSONDecodeError:
            print('Error reading the config file. Using defaults.')
            return DEFAULT_CONFIG
    return {**DEFAULT_CONFIG, **user_config}

# Example usage if needed:
# config = load_config('config.json')
# print(config)