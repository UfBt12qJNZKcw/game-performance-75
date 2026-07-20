import random
import json

class GameProcessor:
    def __init__(self):
        self.score = 0
        self.max_score = 100

    def process_input(self, user_input):
        if self.validate_input(user_input):
            self.score += int(user_input)
            if self.score > self.max_score:
                self.score = self.max_score
            return self.get_status()
        else:
            return json.dumps({'error': 'Invalid input'});

    def validate_input(self, user_input):
        try:
            value = int(user_input)
            return 0 <= value <= 10  # Allow input from 0 to 10
        except ValueError:
            return False

    def get_status(self):
        return json.dumps({'score': self.score, 'status': 'Running'})

if __name__ == '__main__':
    gp = GameProcessor()
    while True:
        user_input = input('Enter your input (0-10): ')
        status = gp.process_input(user_input)
        print(status)