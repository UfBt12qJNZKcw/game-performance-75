class GameError(Exception):
    """Custom exception for game-related errors."""
    def __init__(self, message, *args):
        super().__init__(message, *args)
        self.message = message

    def __str__(self):
        return f"GameError: {self.message}"

class PlayerNotFoundError(GameError):
    """Exception raised when a player is not found."""
    def __init__(self, player_id):
        super().__init__(f'Player with ID {player_id} not found.')
        self.player_id = player_id

class InvalidMoveError(GameError):
    """Exception raised for invalid game moves."""
    def __init__(self, move):
        super().__init__(f'Move {move} is not allowed.')
        self.move = move

class GameNotFoundError(GameError):
    """Exception raised when a game session is not found."""
    def __init__(self, game_id):
        super().__init__(f'Game with ID {game_id} not found.')
        self.game_id = game_id