import logging
import os
from logging.handlers import RotatingFileHandler

LOG_FILE = 'game_performance.log'
LOG_LEVEL = logging.INFO

def setup_logger():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w') as f:
            pass

    logger = logging.getLogger('GamePerformanceLogger')
    logger.setLevel(LOG_LEVEL)

    handler = RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger

# Example usage
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger setup complete.')