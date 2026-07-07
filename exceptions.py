class GameError(Exception):
    """Base class for game-specific exceptions."""
    pass

class ResourceNotFoundError(GameError):
    """Raised when a game resource is not found."""
    def __init__(self, resource_name):
        super().__init__(f'Resource not found: {resource_name}')
        self.resource_name = resource_name

class InvalidGameStateError(GameError):
    """Raised when an operation is performed that is invalid for the current game state."""
    def __init__(self, current_state, attempted_action):
        super().__init__(f'Invalid action: {attempted_action} in state: {current_state}')
        self.current_state = current_state
        self.attempted_action = attempted_action

class ScoreLimitExceededError(GameError):
    """Raised when a score exceeds the allowed limit."""
    def __init__(self, score, limit):
        super().__init__(f'Score {score} exceeds limit {limit}')
        self.score = score
        self.limit = limit

class NetworkError(GameError):
    """Raised for network-related errors during multiplayer sessions."""
    def __init__(self, message):
        super().__init__(message)