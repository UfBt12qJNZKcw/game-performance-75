import sys
import json

class InputError(Exception):
    pass

class GameProcessor:
    def __init__(self):
        self.valid_inputs = ['start', 'stop', 'pause', 'resume']
    
    def validate_input(self, user_input):
        if user_input not in self.valid_inputs:
            raise InputError(f"Invalid command: {user_input}")

    def process_command(self, command):
        self.validate_input(command)
        print(f"Processing command: {command}")

    def main_loop(self):
        while True:
            user_input = input("Enter command: ").strip().lower()
            try:
                self.process_command(user_input)
            except InputError as e:
                print(e)
            except KeyboardInterrupt:
                print("Exiting program...")
                sys.exit(0)

if __name__ == '__main__':
    processor = GameProcessor()
    processor.main_loop()