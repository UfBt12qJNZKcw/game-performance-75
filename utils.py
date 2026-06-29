import json

class GamingDataError(Exception):
    pass


def load_game_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise GamingDataError('File not found')
    except json.JSONDecodeError:
        raise GamingDataError('Invalid JSON format')


def save_game_data(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise GamingDataError(f'Error saving data: {str(e)}')


def update_game_data(file_path, new_data):
    try:
        data = load_game_data(file_path)
        data.update(new_data)
        save_game_data(file_path, data)
    except GamingDataError as e:
        print(e)


def get_high_scores(data, top_n=5):
    return sorted(data, key=lambda x: x['score'], reverse=True)[:top_n}
