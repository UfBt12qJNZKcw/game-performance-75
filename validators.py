def validate_input(user_input):
    allowed_inputs = {'move_up', 'move_down', 'move_left', 'move_right', 'attack', 'defend'}
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string.')
    if user_input not in allowed_inputs:
        raise ValueError(f'Invalid input: {user_input}. Allowed inputs: {allowed_inputs}')
    return True

def main_game_loop():
    while True:
        try:
            user_input = input('Enter your action: ')
            # Validate the user input
            validate_input(user_input)
            process_input(user_input)
        except ValueError as e:
            print(e)
            continue

def process_input(user_input):
    print(f'Processing input: {user_input}')

if __name__ == '__main__':
    main_game_loop()