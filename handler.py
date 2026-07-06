import random

class GameHandler:
    def __init__(self):
        self.valid_input_range = (1, 100)

    def get_user_input(self):
        while True:
            try:
                user_input = int(input("Enter a number between 1 and 100: "))
                if user_input < self.valid_input_range[0] or user_input > self.valid_input_range[1]:
                    raise ValueError('Input out of range')
                return user_input
            except ValueError as e:
                print(f'Invalid input: {e}. Please try again.')

    def process_input(self, user_input):
        # Simple game logic determining if guess is too high, too low, or correct
        target_number = random.randint(self.valid_input_range[0], self.valid_input_range[1])
        print(f'Target number is: {target_number}')  # For testing purposes

        if user_input < target_number:
            return 'Too low!'
        elif user_input > target_number:
            return 'Too high!'
        else:
            return 'Correct!'

    def main_loop(self):
        while True:
            user_input = self.get_user_input()
            result = self.process_input(user_input)
            print(result)
            if result == 'Correct!':
                break

if __name__ == '__main__':
    game_handler = GameHandler()
    game_handler.main_loop()