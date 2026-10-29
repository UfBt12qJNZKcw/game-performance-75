import logging
from logging.handlers import RotatingFileHandler
import os

def get_performance_logger(name='game-perf', log_file='performance.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | [%(name)s] %(message)s'
        )
        
        # 5MB rotation, keeps 3 historical files
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5*1024*1024, 
            backupCount=3
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        # Console stream for local dev observation
        stream = logging.StreamHandler()
        stream.setFormatter(formatter)
        logger.addHandler(stream)
        
    return logger

# Instantiate singleton-like logger for global game use
perf_logger = get_performance_logger()