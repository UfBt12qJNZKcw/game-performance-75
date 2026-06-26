import random

class GameHandler:
    def __init__(self):
        self.valid_inputs = ['move', 'attack', 'defend', 'run']

    def validate_input(self, user_input):
        return user_input in self.valid_inputs

    def main_loop(self):
        while True:
            user_input = input('Enter your command: ').strip().lower()
            if self.validate_input(user_input):
                self.process_input(user_input)
            else:
                print('Invalid command! Please try again.')

    def process_input(self, command):
        if command == 'move':
            print('You move forward.')
        elif command == 'attack':
            print('You attack!')
        elif command == 'defend':
            print('You take a defensive stance.')
        elif command == 'run':
            print('You run away.')</code>