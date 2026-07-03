import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class GameLogger:
    """Custom logger for game events."""

    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def log_event(self, event_type, message):
        if event_type.lower() not in ['info', 'debug', 'error']:
            raise ValueError('Invalid event type')
        if not isinstance(message, str) or not message:
            raise ValueError('Message must be a non-empty string')
        
        log_method = getattr(self.logger, event_type.lower())
        log_method(message)

    def log_error(self, message):
        self.log_event('error', message)

    def log_info(self, message):
        self.log_event('info', message)

    def log_debug(self, message):
        self.log_event('debug', message)

# Example usage
if __name__ == '__main__':
    game_logger = GameLogger('GamePerformance')
    game_logger.log_info('Game started')
    game_logger.log_debug('Loading assets')
    game_logger.log_error('Failed to load asset')
