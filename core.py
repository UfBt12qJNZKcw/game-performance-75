import random
import json

def get_user_input(prompt, valid_inputs):
    user_input = input(prompt)
    while user_input not in valid_inputs:
        print(f"Invalid input. Please choose from {valid_inputs}.")
        user_input = input(prompt)
    return user_input

def main_game_loop():
    actions = ['move', 'shoot', 'reload']
    print("Welcome to the game!")
    while True:
        user_action = get_user_input("Choose your action (move/shoot/reload): ", actions)
        process_action(user_action)

    print("Thanks for playing!")

def process_action(action):
    if action == 'move':
        print("You move forward!")
    elif action == 'shoot':
        print("Bang! You've shot your weapon!")
    elif action == 'reload':
        print("You reload your weapon.")

if __name__ == '__main__':
    main_game_loop()