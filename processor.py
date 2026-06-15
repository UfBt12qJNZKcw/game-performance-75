import json
import random

class GameProcessor:
    def __init__(self):
        self.valid_inputs = ['attack', 'defend', 'heal']

    def validate_input(self, user_input):
        return user_input in self.valid_inputs

    def process_input(self, user_input):
        if not self.validate_input(user_input):
            raise ValueError('Invalid input!')
        # Simulate game action processing
        return f'Processed action: {user_input}'

    def main_loop(self):
        while True:
            user_input = input('Enter your action (attack, defend, heal or exit): ').strip().lower()
            if user_input == 'exit':
                print('Exiting game. Goodbye!')
                break
            try:
                result = self.process_input(user_input)
                print(result)
            except ValueError as e:
                print(e)

if __name__ == '__main__':
    game = GameProcessor()
    game.main_loop()