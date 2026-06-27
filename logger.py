import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='game.log', max_size=5*1024*1024, backup_count=3):
    if not os.path.exists(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file))
    
    logger = logging.getLogger('game_logger')
    logger.setLevel(logging.DEBUG)
    
    handler = RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger

if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger has been set up.')