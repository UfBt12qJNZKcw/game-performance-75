import json
import random

class GameProcessor:
    def __init__(self):
        self.players = []

    def add_player(self, name):
        if not isinstance(name, str) or not name:
            raise ValueError('Invalid player name')
        self.players.append(name)

    def simulate_game(self):
        if len(self.players) < 2:
            raise ValueError('Not enough players to start a game')
        winner = random.choice(self.players)
        return {'winner': winner, 'player_count': len(self.players)}

    def reset_game(self):
        self.players.clear()
        return 'Game has been reset'

    def get_player_list(self):
        if not self.players:
            return 'No players available'
        return self.players

if __name__ == '__main__':
    processor = GameProcessor()
    try:
        processor.add_player('Alice')
        processor.add_player('Bob')
        print(processor.simulate_game())
    except ValueError as e:
        print(f'Error: {e}')
    
    print(processor.get_player_list())
    
    processor.reset_game()