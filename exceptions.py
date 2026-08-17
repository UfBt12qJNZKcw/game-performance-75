class GameError(Exception):
    """Base class for game-related exceptions."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class LevelNotFoundError(GameError):
    """Exception raised when a game level is not found."""
    def __init__(self, level_id):
        super().__init__(f'Level {level_id} does not exist.')
        self.level_id = level_id

class InvalidPlayerActionError(GameError):
    """Exception raised for invalid actions by players."""
    def __init__(self, action):
        super().__init__(f'Action {action} is not valid.')
        self.action = action

class ConnectionError(GameError):
    """Exception raised for connection issues."""
    def __init__(self, details):
        super().__init__(f'Connection failed: {details}')
        self.details = details

class GameTimeoutError(GameError):
    """Exception raised when a game operation times out."""
    def __init__(self, timeout):
        super().__init__(f'Operation timed out after {timeout} seconds.')
        self.timeout = timeout

