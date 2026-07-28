class GameError(Exception):
    """Base class for exceptions in the game."""
    pass

class InvalidDataError(GameError):
    """Raised when the game data is invalid."""
    def __init__(self, message, data):
        self.message = message
        self.data = data
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.data}'

class UnsupportedFormatError(GameError):
    """Raised for unsupported data formats."""
    def __init__(self, format_type):
        self.format_type = format_type
        self.message = f'Unsupported data format: {self.format_type}'
        super().__init__(self.message)

    def __str__(self):
        return self.message

class GameNotFoundError(GameError):
    """Raised when the specified game is not found."""
    def __init__(self, game_id):
        self.game_id = game_id
        self.message = f'Game with ID {self.game_id} not found.'
        super().__init__(self.message)

    def __str__(self):
        return self.message