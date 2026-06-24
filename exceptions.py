class GameError(Exception):
    """Base class for exceptions in game operations."""
    pass

class InvalidMoveError(GameError):
    """Exception raised for invalid moves in the game."""
    def __init__(self, message="Invalid move attempted."):
        self.message = message
        super().__init__(self.message)

class GameStateError(GameError):
    """Exception raised when game state is inconsistent."""
    def __init__(self, message="Game state is not valid."):
        self.message = message
        super().__init__(self.message)

class PlayerError(GameError):
    """Exception raised for player-related errors."""
    def __init__(self, player_id, message="Player error occurred."):
        self.player_id = player_id
        self.message = f"{message} (Player ID: {player_id})"
        super().__init__(self.message)

class NetworkError(GameError):
    """Exception raised for network-related issues."""
    def __init__(self, message="Network error occurred."):
        self.message = message
        super().__init__(self.message)