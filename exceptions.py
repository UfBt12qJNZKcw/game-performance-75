class GameError(Exception):
    """Base class for exceptions in this game."""
    pass

class InvalidInputError(GameError):
    """Raised for invalid inputs."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ResourceNotFoundError(GameError):
    """Raised when a resource is not found."""
    def __init__(self, resource):
        self.resource = resource
        self.message = f'Resource {resource} not found.'
        super().__init__(self.message)

class GameLogicError(GameError):
    """Raised for logical errors within game processing."""
    def __init__(self, logic_issue):
        self.logic_issue = logic_issue
        self.message = f'Game logic error occurred: {logic_issue}'
        super().__init__(self.message)