import json
import os

def load_game_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {file_path}")
        return {}


def save_game_data(file_path, data):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def update_game_data(file_path, new_data):
    data = load_game_data(file_path)
    data.update(new_data)
    save_game_data(file_path, data)


def display_game_data(file_path):
    data = load_game_data(file_path)
    print(json.dumps(data, indent=4))

