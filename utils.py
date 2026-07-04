import json
import os

def save_game_data(file_path, data):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def load_game_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as f:
        return json.load(f)


def update_game_data(file_path, updates):
    data = load_game_data(file_path)
    if data is None:
        data = {}
    data.update(updates)
    save_game_data(file_path, data)


def reset_game_data(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)