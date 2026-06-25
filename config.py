import json
import os

def load_config(file_path='config.json', defaults=None):
    if defaults is None:
        defaults = {}
    # Check if the config file exists
    if not os.path.isfile(file_path):
        return defaults
    with open(file_path, 'r') as file:
        try:
            config = json.load(file)
        except json.JSONDecodeError:
            print('Invalid JSON in config file. Using defaults.')</code>
            return defaults
    # Merge defaults with configurations, allowing overrides
    config = {**defaults, **config}
    return config

# Usage Example:
if __name__ == '__main__':
    default_config = {'volume': 70, 'resolution': '1920x1080'}
    config = load_config('config.json', default_config)
    print(config)