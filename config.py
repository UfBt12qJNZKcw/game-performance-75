import os
import json

class ConfigError(Exception):
    pass

def load_config(filepath):
    if not os.path.isfile(filepath):
        raise ConfigError(f"Configuration file not found: {filepath}")
    try:
        with open(filepath, 'r') as file:
            config = json.load(file)
    except json.JSONDecodeError as e:
        raise ConfigError(f"Error decoding JSON: {str(e)}")
    except Exception as e:
        raise ConfigError(f"Unexpected error: {str(e)}")
    validate_config(config)
    return config

def validate_config(config):
    required_keys = ['setting1', 'setting2', 'setting3']
    for key in required_keys:
        if key not in config:
            raise ConfigError(f"Missing required config key: {key}")

# Example usage
if __name__ == '__main__':
    try:
        config = load_config('config.json')
        print(config)
    except ConfigError as e:
        print(f'Configuration error: {e}')
