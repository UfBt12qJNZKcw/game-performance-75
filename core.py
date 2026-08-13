import random

class GameError(Exception):
    pass

class Game:
    def __init__(self):
        self.score = 0
        self.level = 1

    def play(self):
        try:
            self.start_game()
        except GameError as e:
            print(f'Game error occurred: {e}')

    def start_game(self):
        trying_level = random.choice([1, 0, -1])  # Simulate levels
        if trying_level < 0:
            raise GameError('Invalid level selection')
        self.level = trying_level
        self.simulate_gameplay()

    def simulate_gameplay(self):
        if self.level == 0:
            raise GameError('Level cannot be zero')
        for _ in range(5):  # simulate 5 rounds of gameplay
            self.score += random.randint(1, 10)
        print(f'Final score: {self.score} on level {self.level}')

if __name__ == '__main__':
    game = Game()
    game.play()