def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError("Input must be a string")
    if not user_input.strip():
        raise ValueError("Input cannot be empty or whitespace")
    if len(user_input) < 3:
        raise ValueError("Input must be at least 3 characters long")
    if len(user_input) > 50:
        raise ValueError("Input must not exceed 50 characters")
    return True

def main_processing_loop():
    while True:
        user_input = input("Enter command: ")
        try:
            validate_input(user_input)
            print(f"Valid input received: {user_input}")
            # Proceed with game logic here
        except ValueError as e:
            print(f"Input error: {e}")
            continue

if __name__ == "__main__":
    main_processing_loop()