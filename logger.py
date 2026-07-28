import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='game.log', max_bytes=5 * 1024 * 1024, backup_count=5):
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    logger = logging.getLogger('GameLogger')
    logger.setLevel(logging.DEBUG)
    
    handler = RotatingFileHandler(os.path.join('logs', log_file), maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger

# Example usage
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger is set up and ready.')