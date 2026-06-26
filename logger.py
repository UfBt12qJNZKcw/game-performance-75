import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='game.log', max_bytes=5*1024*1024, backup_count=3):
    logger = logging.getLogger('game_logger')
    logger.setLevel(logging.DEBUG)

    if not logger.hasHandlers():
        # Create rotation handler
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # Add handler to the logger
        logger.addHandler(handler)

    return logger

# Example usage:
# logger = setup_logger()
# logger.info('This is an info message')