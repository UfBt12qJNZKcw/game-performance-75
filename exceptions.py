class GameError(Exception):
    """Base class for all game-related exceptions."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class PlayerNotFound(GameError):
    """Exception raised when a player cannot be found."""
    def __init__(self, player_id):
        super().__init__(f'Player with ID {player_id} not found.')
        self.player_id = player_id

class GameNotFound(GameError):
    """Exception raised when a game cannot be found."""
    def __init__(self, game_id):
        super().__init__(f'Game with ID {game_id} not found.')
        self.game_id = game_id

class InvalidScoreError(GameError):
    """Exception raised for invalid score submissions."""
    def __init__(self, score):
        super().__init__(f'Invalid score: {score}. Score must be non-negative.')
        self.score = score

class QuotaExceededError(GameError):
    """Exception raised when player exceeds action quota."""
    def __init__(self, action):
        super().__init__(f'Action quota exceeded for {action}.')
        self.action = action
