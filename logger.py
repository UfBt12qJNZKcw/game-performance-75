import logging
from logging.handlers import RotatingFileHandler

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create handlers
handler = RotatingFileHandler('game_performance.log', maxBytes=5*1024*1024, backupCount=5)
handler.setLevel(logging.DEBUG)

# Create formatters and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(handler)

# Simple test logging
if __name__ == '__main__':
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
