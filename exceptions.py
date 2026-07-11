class GameError(Exception):
    pass

class ConnectionError(GameError):
    def __init__(self, message='Unable to connect to the game server.'):
        super().__init__(message)

class ValidationError(GameError):
    def __init__(self, message='Validation failed for provided data.'): 
        super().__init__(message)

class ResourceNotFound(GameError):
    def __init__(self, resource):
        message = f'Resource {resource} not found.'
        super().__init__(message)

class PerformanceException(GameError):
    def __init__(self, performance_metric):
        message = f'Performance issue detected: {performance_metric}'
        super().__init__(message)

def check_resource(resource):
    if resource is None:
        raise ResourceNotFound('Game asset')

def validate_score(score):
    if not (0 <= score <= 100):
        raise ValidationError(f'Score {score} is out of range [0-100].')