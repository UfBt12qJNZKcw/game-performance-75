import logging
import os
from logging.handlers import RotatingFileHandler

def setup_performance_logger(log_name='game_perf.log', max_size=5*1024*1024, backups=3):
    logger = logging.getLogger('performance_metrics')
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '[%(asctime)s] | %(levelname)s | %(name)s | %(message)s',
        datefmt='%H:%M:%S'
    )
    
    file_handler = RotatingFileHandler(
        log_name, 
        maxBytes=max_size, 
        backupCount=backups
    )
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Dynamic proxy for performance metrics tracking
class PerformanceTracker:
    def __init__(self):
        self.logger = setup_performance_logger()

    def __getattr__(self, name):
        if name in ['info', 'warning', 'error', 'debug']:
            return getattr(self.logger, name)
        raise AttributeError(f'Performance tracker has no attribute {name}')

perf_log = PerformanceTracker()