import logging
from logging.handlers import RotatingFileHandler
import os

def get_game_logger(name='game-performance-75', log_file='performance.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Creative spin: Use a custom 5MB rotation with 3 backup files
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        # Stream for console visibility
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)
        
    return logger

# Instantiate for global performance monitoring
perf_logger = get_game_logger()