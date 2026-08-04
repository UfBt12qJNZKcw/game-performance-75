class GameError(Exception):
    pass

class InvalidInputError(GameError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class OutOfBoundsError(GameError):
    def __init__(self, position):
        self.position = position
        self.message = f"Position {self.position} is out of bounds"
        super().__init__(self.message)

class GameStateError(GameError):
    def __init__(self, state):
        self.state = state
        self.message = f"Invalid game state: {self.state}"
        super().__init__(self.message)

def handle_game_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except GameError as e:
            print(f'Game Error: {e.message}')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
    return wrapper
