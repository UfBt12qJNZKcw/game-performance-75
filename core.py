import random

class Game:
    def __init__(self):
        self.score = 0
        self.player_health = 100
        self.valid_actions = ['attack', 'defend', 'heal']

    def validate_input(self, action):
        return action in self.valid_actions

    def process_action(self, action):
        if not self.validate_input(action):
            raise ValueError(f'Invalid action: {action}')
        if action == 'attack':
            self.score += random.randint(5, 10)
            print(f'You attacked! Score: {self.score}')
        elif action == 'defend':
            self.player_health -= random.randint(1, 5)
            print(f'You defended! Health: {self.player_health}')
        elif action == 'heal':
            self.player_health += random.randint(5, 15)
            print(f'You healed! Health: {self.player_health}')

    def main_loop(self):
        while self.player_health > 0:
            action = input('Enter your action (attack, defend, heal): ').strip().lower()
            try:
                self.process_action(action)
            except ValueError as ve:
                print(ve)
        print('Game Over!')

if __name__ == '__main__':
    game = Game()
    game.main_loop()