import random
import sys

def game_loop():
    print("Welcome to the game! Please enter your commands.")
    while True:
        user_input = input("> ").strip().lower()
        if validate_input(user_input):
            process_input(user_input)
        else:
            print("Invalid input, please try again.")
            continue
        if user_input in ['exit', 'quit']:
            print("Exiting game...")
            break

def validate_input(user_input):
    valid_commands = ['move', 'attack', 'defend', 'quit', 'exit']
    return user_input in valid_commands

def process_input(user_input):
    if user_input == 'move':
        print("You move forward.")
    elif user_input == 'attack':
        print("You attack your enemy.")
    elif user_input == 'defend':
        print("You brace for an attack.")
    else:
        print("Command not recognized.")

if __name__ == '__main__':
    game_loop()