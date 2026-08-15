import sys
import random

def process_input(user_input):
    if not user_input.isdigit():
        raise ValueError("Input must be a number")
    value = int(user_input)
    if value < 1 or value > 100:
        raise ValueError("Input must be between 1 and 100")
    return value

def main_loop():
    while True:
        user_input = input("Enter a number (1-100) or 'exit' to quit: ")
        if user_input.lower() == 'exit':
            print("Exiting game.")
            break
        try:
            valid_number = process_input(user_input)
            print(f"You entered: {valid_number}")
            # Simulate game processing with the valid number
            game_result = random.randint(1, 100)
            if valid_number == game_result:
                print("Congratulations! You guessed it!")
            else:
                print(f"Sorry, the correct number was {game_result}.")
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    main_loop()