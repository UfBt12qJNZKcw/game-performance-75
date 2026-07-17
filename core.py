import random
import time

class Game:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f'Game {self.name} has started!')

    def play(self):
        if not self.is_running:
            print('Game is not started yet!')
            return
        while self.score < 10:
            score_increment = random.randint(1, 3)
            self.score += score_increment
            print(f'Score incremented by {score_increment}. Current score: {self.score}')
            time.sleep(1)
        print('Congratulations, you reached the score of 10!')
        self.is_running = False


if __name__ == '__main__':
    game = Game('Adventures')
    game.start()
    game.play()