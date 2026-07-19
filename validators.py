def validate_input(input_value):
    if not isinstance(input_value, (int, float)):
        raise ValueError('Input must be a number')
    if input_value < 0:
        raise ValueError('Input must be a non-negative number')
    return True

def main_loop():
    while True:
        user_input = input('Enter a number for processing: ')
        try:
            processed_input = float(user_input)
            validate_input(processed_input)
            print(f'Processing: {processed_input}')
            # Insert main processing logic here
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            print('\nExiting the game loop.')
            break

if __name__ == '__main__':
    main_loop()