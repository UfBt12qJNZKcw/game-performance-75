class GameException(Exception):
    """Base class for game-specific exceptions."""
    pass

class InvalidInputError(GameException):
    """Exception raised for invalid input errors."""
    def __init__(self, message="Invalid input provided."):
        self.message = message
        super().__init__(self.message)

class ResourceNotFoundError(GameException):
    """Exception raised when a resource is not found."""
    def __init__(self, resource_name):
        self.message = f'Resource {resource_name} not found.'
        super().__init__(self.message)

class GameOverError(GameException):
    """Exception raised when a game is over."""
    def __init__(self):
        self.message = 'The game is over, no more moves allowed.'
        super().__init__(self.message)

class NetworkError(GameException):
    """Exception raised for network-related errors."""
    def __init__(self, message="Network connection issue."):
        self.message = message
        super().__init__(self.message)
