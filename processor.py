import random

class GameProcessor:
    def __init__(self):
        self.players = []

    def add_player(self, player_name):
        if not isinstance(player_name, str) or not player_name:
            raise ValueError('Player name must be a non-empty string.')
        if player_name in self.players:
            raise ValueError('Player already exists.')
        self.players.append(player_name)

    def start_game(self):
        if len(self.players) < 2:
            raise RuntimeError('Not enough players to start the game.')
        random.shuffle(self.players)
        print(f'Game starting with players: {self.players}')

    def remove_player(self, player_name):
        if player_name not in self.players:
            raise ValueError('Player does not exist.')
        self.players.remove(player_name)

    def get_player_count(self):
        return len(self.players)

    def reset_game(self):
        self.players.clear()

if __name__ == '__main__':
    processor = GameProcessor()
    try:
        processor.add_player('Alice')
        processor.add_player('Bob')
        processor.start_game()
    except Exception as e:
        print(f'Error occurred: {e}')