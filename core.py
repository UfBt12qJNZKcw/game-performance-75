import random
import sys

class GameError(Exception):
    pass

class Game:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.is_running = True

    def start(self):
        try:
            self.play()
        except GameError as e:
            self.handle_error(e)
        except Exception as e:
            self.handle_unexpected_error(e)

    def play(self):
        while self.is_running:
            self.level_up()
            action = random.choice(['win', 'lose', 'error', 'continue'])
            if action == 'win':
                self.score += 10
                print(f'Level {self.level}: You win! Score: {self.score}')
            elif action == 'lose':
                self.score -= 10
                print(f'Level {self.level}: You lose! Score: {self.score}')
            elif action == 'error':
                raise GameError('A game-specific error occurred!')
            else:
                print(f'Level {self.level}: No action taken.')

    def level_up(self):
        if self.score < 0:
            raise GameError('Score cannot be negative.')
        self.level += 1

    def handle_error(self, error):
        print(f'Handling game error: {error}')
        self.is_running = False

    def handle_unexpected_error(self, error):
        print(f'Unexpected error occurred: {error}', file=sys.stderr)
        self.is_running = False

if __name__ == '__main__':
    game = Game()
    game.start()  
