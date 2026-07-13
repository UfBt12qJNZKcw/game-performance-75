import time
import random

class Game:
    def __init__(self):
        self.players = []
        self.scoreboard = {}

    def add_player(self, player):
        self.players.append(player)
        self.scoreboard[player] = 0

    def play_round(self):
        round_scores = {player: random.randint(1, 100) for player in self.players}
        self.update_scores(round_scores)

    def update_scores(self, round_scores):
        for player, score in round_scores.items():
            self.scoreboard[player] += score
            print(f'{player} scored {score}. Total: {self.scoreboard[player]}')

    def get_winner(self):
        winner = max(self.scoreboard, key=self.scoreboard.get)
        return winner, self.scoreboard[winner]

    def start_game(self, rounds):
        for _ in range(rounds):
            self.play_round()
        winner, score = self.get_winner()
        print(f'Winner is {winner} with score {score}')

if __name__ == '__main__':
    game = Game()
    game.add_player('Alice')
    game.add_player('Bob')
    game.start_game(5)