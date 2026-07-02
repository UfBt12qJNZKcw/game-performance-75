import random
import logging

class Game:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.score = {player: 0 for player in players}
        self.max_score = 100
        logging.basicConfig(level=logging.INFO)

    def play_round(self):
        try:
            if len(self.players) < 2:
                raise ValueError('At least two players are required')
            round_scores = {player: random.randint(1, 10) for player in self.players}
            logging.info(f'Round scores: {round_scores}')
            self.update_score(round_scores)
        except ValueError as ve:
            logging.error(f'ValueError: {ve}')
        except Exception as e:
            logging.error(f'An unexpected error occurred: {e}')

    def update_score(self, round_scores):
        for player, score in round_scores.items():
            self.score[player] += score
            if self.score[player] >= self.max_score:
                self.end_game(player)

    def end_game(self, winner):
        logging.info(f'{winner} wins the game!')
        self.score = {player: 0 for player in self.players}

if __name__ == '__main__':
    game = Game('My Game', ['Alice', 'Bob'])
    for _ in range(15):
        game.play_round()