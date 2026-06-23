class GameError(Exception):
    """Base class for all game errors."""
    pass

class InvalidMoveError(GameError):
    """Raised when a player makes an invalid move."""
    def __init__(self, move, message="Invalid move attempted."):
        self.move = move
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} Move: {self.move}'

class ScoreOutOfRangeError(GameError):
    """Raised when the score is not within a valid range."""
    def __init__(self, score, min_score=0, max_score=100, message="Score out of valid range."):
        self.score = score
        self.min_score = min_score
        self.max_score = max_score
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} Score: {self.score}, Expected range: [{self.min_score}, {self.max_score}]'

# Usage examples
try:
    raise InvalidMoveError('Z3')
except InvalidMoveError as e:
    print(e)

try:
    raise ScoreOutOfRangeError(150, 0, 100)
except ScoreOutOfRangeError as e:
    print(e)