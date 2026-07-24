class InputValidationError(Exception):
    pass

class GameProcessor:
    def __init__(self):
        self.valid_inputs = set(['move', 'attack', 'defend', 'quit'])

    def process_input(self, user_input):
        if not self.is_valid_input(user_input):
            raise InputValidationError(f'Invalid input: {user_input}')
        print(f'Processing: {user_input}')  # Simulating action

    def is_valid_input(self, user_input):
        return user_input in self.valid_inputs

    def main_loop(self):
        while True:
            user_input = input('Enter action (move, attack, defend, quit): ')
            try:
                self.process_input(user_input)
                if user_input == 'quit':
                    break
            except InputValidationError as e:
                print(str(e))
                print('Please try again.')