import json
import os

def load_config(file_path, defaults):
    if not os.path.exists(file_path):
        return defaults
    with open(file_path, 'r') as f:
        config = json.load(f)
    return {**defaults, **config}

# Default configuration
DEFAULTS = {
    'window_size': (800, 600),
    'fullscreen': False,
    'volume': 0.5,
    'language': 'en',
}

# Load the configuration
config_file_path = 'config.json'
config = load_config(config_file_path, DEFAULTS)

if __name__ == '__main__':
    print('Loaded Configuration:')
    print(config)