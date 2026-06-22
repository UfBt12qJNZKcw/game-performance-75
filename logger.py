import logging
from logging.handlers import RotatingFileHandler

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_FILE = 'game_performance.log'

# Logger configuration function
def setup_logger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=5)
    formatter = logging.Formatter(LOG_FORMAT)
    handler.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(handler)
    return logger

# Example usage
if __name__ == '__main__':
    game_logger = setup_logger('game_logger')
    game_logger.info('Game started!')
    game_logger.warning('Low memory warning!')
    game_logger.error('Game crashed!')