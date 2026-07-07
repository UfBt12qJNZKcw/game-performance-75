import random
import sys

class Game:
    def __init__(self):
        self.score = 0
        self.max_score = 100
        self.min_score = 0

    def process_input(self, user_input):
        try:
            value = int(user_input)
            if self.min_score <= value <= self.max_score:
                self.score = value
                print(f'Score updated to: {self.score}')
            else:
                raise ValueError('Input must be between 0 and 100.')
        except ValueError as e:
            print(f'Invalid input: {e}')

    def main_loop(self):
        while True:
            user_input = input('Enter your score (0-100) or type exit to quit: ')
            if user_input.lower() == 'exit':
                print('Exiting game...')
                break
            self.process_input(user_input)

if __name__ == '__main__':
    game = Game()
    game.main_loop()