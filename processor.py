import random
import json

def process_game_input(user_input):
    valid_inputs = ['move', 'attack', 'defend', 'heal']
    if user_input not in valid_inputs:
        raise ValueError("Invalid input. Please choose from: move, attack, defend, heal.")
    return f'Processing action: {user_input}'

def main_processing_loop():
    while True:
        user_input = input("Enter your action (move, attack, defend, heal) or 'quit' to exit: ").strip().lower()
        if user_input == 'quit':
            print('Exiting game. Goodbye!')
            break
        try:
            result = process_game_input(user_input)
            print(result)
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    main_processing_loop()