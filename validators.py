def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string.')
    if not user_input:
        raise ValueError('Input cannot be empty.')
    if any(char.isdigit() for char in user_input):
        raise ValueError('Input must not contain numbers.')
    return True

def validate_choice(choice, valid_choices):
    if choice not in valid_choices:
        raise ValueError(f'Invalid choice: {choice}. Valid choices are: {valid_choices}')
    return True

if __name__ == '__main__':
    valid_choices = ['rock', 'paper', 'scissors']
    try:
        user_input = input('Enter your choice: ')
        validate_input(user_input)
        validate_choice(user_input, valid_choices)
        print('Input is valid, processing...')
    except ValueError as e:
        print(f'Error: {e}')