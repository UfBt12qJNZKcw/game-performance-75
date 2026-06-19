class GameError(Exception):
    """Base class for game-related exceptions."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class HighScoreError(GameError):
    """Raised when there is an error with high score handling."""
    def __init__(self, message="High score could not be processed."):
        super().__init__(message)

class PlayerError(GameError):
    """Raised when there is an issue with player actions."""
    def __init__(self, message="Player action is invalid."):
        super().__init__(message)

class LevelError(GameError):
    """Raised when there is an error loading or processing game levels."""
    def __init__(self, message="Level data is corrupted or missing."):
        super().__init__(message)

class GameLoadError(GameError):
    """Raised when the game fails to load."""
    def __init__(self, message="Game resources could not be loaded."):
        super().__init__(message)