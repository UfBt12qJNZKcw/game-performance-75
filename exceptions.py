class GameError(Exception):
    pass

class NotFoundError(GameError):
    def __init__(self, item):
        super().__init__(f'{item} not found')

class InvalidMoveError(GameError):
    def __init__(self, move):
        super().__init__(f'Invalid move: {move}')

class TimeoutError(GameError):
    def __init__(self, duration):
        super().__init__(f'Timed out after {duration} seconds')

class InsufficientResourcesError(GameError):
    def __init__(self, resource):
        super().__init__(f'Insufficient {resource} available')

class AuthenticationError(GameError):
    def __init__(self, user):
        super().__init__(f'Authentication failed for user: {user}')
