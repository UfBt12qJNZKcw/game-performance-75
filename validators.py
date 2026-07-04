def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if not user_input:
        raise ValueError('Input cannot be empty')
    if len(user_input) > 100:
        raise ValueError('Input exceeds maximum length of 100 characters')
    return True

def main_process_loop():
    while True:
        user_input = input('Enter your command: ')
        try:
            validate_input(user_input)
            # Process input here
            print(f'Processing: {user_input}')
        except ValueError as e:
            print(f'Input error: {e}')

if __name__ == '__main__':
    main_process_loop()