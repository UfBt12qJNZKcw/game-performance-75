import logging
from logging.handlers import RotatingFileHandler
import os

def get_game_logger(name='performance-75'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if logger.hasHandlers():
        return logger
    
    formatter = logging.Formatter(
        '[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )

    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    file_handler = RotatingFileHandler(
        filename=os.path.join(log_dir, f'{name}.log'),
        maxBytes=1024 * 1024 * 5,
        backupCount=3
    )
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

log = get_game_logger()