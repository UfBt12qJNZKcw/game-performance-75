class GameError(Exception):
    """Base class for exceptions in the game."""
    pass

class InvalidMoveError(GameError):
    """Raised when a move is invalid."""
    def __init__(self, message="Invalid move attempted."):
        self.message = message
        super().__init__(self.message)

class PlayerNotFoundError(GameError):
    """Raised when a specified player is not found."""
    def __init__(self, player_name):
        self.message = f"Player '{player_name}' not found."
        super().__init__(self.message)

class GameAlreadyStartedError(GameError):
    """Raised when trying to modify a game in progress."""
    def __init__(self):
        self.message = "Game has already started."
        super().__init__(self.message)

class InsufficientResourcesError(GameError):
    """Raised when a player lacks resources to perform an action."""
    def __init__(self, resource):
        self.message = f"Insufficient resources: {resource}."
        super().__init__(self.message)