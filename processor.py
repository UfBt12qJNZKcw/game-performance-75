import sys

class GameProcessor:
    def __init__(self):
        self.score = 0

    def validate_input(self, user_input):
        if not user_input.isdigit():
            raise ValueError('Input must be a number')
        if int(user_input) < 0:
            raise ValueError('Input must be a non-negative number')

    def update_score(self, user_input):
        self.validate_input(user_input)
        self.score += int(user_input)
        print(f'Score updated to: {self.score}')

    def main_loop(self):
        while True:
            user_input = input('Enter score to add (or type exit): ')
            if user_input.lower() == 'exit':
                print('Exiting game processor.')
                break
            try:
                self.update_score(user_input)
            except ValueError as e:
                print(e)

if __name__ == '__main__':
    game_processor = GameProcessor()
    game_processor.main_loop()