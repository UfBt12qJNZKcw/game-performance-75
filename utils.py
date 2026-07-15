import json
import random
import time

class GameDataUtil:
    @staticmethod
    def load_game_data(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def save_game_data(file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def generate_random_score(min_score=0, max_score=100):
        return random.randint(min_score, max_score)

    @staticmethod
    def time_stamp():
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    @staticmethod
    def format_game_event(event_name, player, score):
        return f'[{GameDataUtil.time_stamp()}] {player} scored {score} in {event_name}'

if __name__ == '__main__':
    # Example usage of the utility functions.
    scores = []
    for _ in range(5):
        scores.append(GameDataUtil.generate_random_score())
    print(scores)
    print(GameDataUtil.format_game_event('Score Challenge', 'Player1', scores[0]))
    GameDataUtil.save_game_data('game_data.json', {'scores': scores})