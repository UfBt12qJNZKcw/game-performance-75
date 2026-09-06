import logging
from logging.handlers import RotatingFileHandler
import sys

def get_performance_logger(name: str = 'game-performance-75') -> logging.Logger:
    """Initializes a logger with byte-sized rotation for performance tracking."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(name)s] >> %(message)s',
            datefmt='%H:%M:%S'
        )

        # Rotating file handler: 5MB per file, keep 3 backups
        file_handler = RotatingFileHandler(
            'performance.log', 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

# Instantiate singleton for global performance tracing
perf_log = get_performance_logger()