import sys
import json

def input_validation(user_input):
    if not isinstance(user_input, str):
        raise ValueError("Input must be a string")
    if len(user_input) == 0:
        raise ValueError("Input cannot be empty")
    return user_input.strip()

def main_loop():
    while True:
        try:
            user_input = input("Enter command: ")
            validated_input = input_validation(user_input)
            print(f"You entered: {validated_input}")
            if validated_input.lower() == 'exit':
                print("Exiting game.")
                break
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("Game interrupted. Exiting.")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == '__main__':
    main_loop()