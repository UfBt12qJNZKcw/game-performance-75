def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) < 3:
        raise ValueError('Input must be at least 3 characters long')
    if any(char.isdigit() for char in user_input):
        raise ValueError('Input must not contain numbers')
    return True

def game_input_loop():
    while True:
        user_input = input('Enter command: ')
        try:
            validate_input(user_input)
            process_input(user_input)
        except ValueError as e:
            print(f'Input error: {e}')
        except KeyboardInterrupt:
            print('\nExiting game...')
            break

if __name__ == '__main__':
    game_input_loop()