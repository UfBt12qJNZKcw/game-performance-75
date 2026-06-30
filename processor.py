import random
import time

def process_game_input(player_input):
    # This function processes player input
    valid_inputs = ['move', 'jump', 'attack', 'defend']
    if player_input not in valid_inputs:
        raise ValueError(f'Invalid input: {player_input}')
    print(f'Processing input: {player_input}')
    time.sleep(0.5)  # Simulate processing delay
    return f'Input {player_input} processed successfully!'

def main_loop():
    while True:
        try:
            player_input = input('Enter your action (move, jump, attack, defend): ').strip().lower()
            result = process_game_input(player_input)
            print(result)
        except ValueError as ve:
            print(ve)
        except KeyboardInterrupt:
            print('\nExiting game. Goodbye!')
            break
        except Exception as e:
            print(f'An error occurred: {e}')

if __name__ == '__main__':
    main_loop()
