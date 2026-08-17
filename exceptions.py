class InputValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)


def validate_input(user_input):
    if not isinstance(user_input, str):
        raise InputValidationError("Input must be a string")
    if user_input.strip() == "":
        raise InputValidationError("Input cannot be empty")
    if len(user_input) > 100:
        raise InputValidationError("Input must not exceed 100 characters")
    return True


def main_processing_loop():
    while True:
        user_input = input("Enter your command: ")
        try:
            validate_input(user_input)
            print(f"Processing input: {user_input}")
            # Code to process valid input would go here
        except InputValidationError as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    main_processing_loop()