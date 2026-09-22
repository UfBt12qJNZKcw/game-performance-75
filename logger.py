import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='game_engine', log_file='game_perf.log', level=logging.DEBUG):
    """
    Orchestrator for rotating log streams, keeping memory footprint low
    for frame-rate sensitive diagnostic cycles.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | [%(name)s] -> %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # 5MB per log file, keep 3 backups to preserve disk I/O
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )
    
    handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(handler)
        # Add console output for debug sessions
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

# Instantiate the global diagnostic pipeline
debug_logger = setup_logger()