import json

class GameProcessor:
    def __init__(self):
        self.player_actions = []

    def validate_input(self, action):
        valid_actions = {'move', 'attack', 'heal', 'defend'}
        return action in valid_actions

    def process_action(self, action):
        if not self.validate_input(action):
            print(f"Invalid action: {action}")
            return
        self.player_actions.append(action)
        print(f"Action processed: {action}")

    def main_loop(self):
        while True:
            try:
                user_input = input("Enter action (move, attack, heal, defend): ")
                if user_input.lower() == 'exit':
                    break
                self.process_action(user_input.lower())
            except KeyboardInterrupt:
                print("Exiting game...")
                break

if __name__ == '__main__':
    processor = GameProcessor()
    processor.main_loop()