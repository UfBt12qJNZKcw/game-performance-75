import logging
import os
from logging.handlers import RotatingFileHandler

def get_performance_logger(name: str = 'game-perf') -> logging.Logger:
    """Factory for rotatable logs for performance tracking."""
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(process)d | %(message)s'
        )

        # Rotate at 5MB, keep 3 historical snapshots
        file_handler = RotatingFileHandler(
            os.path.join(log_dir, 'perf.log'),
            maxBytes=5*1024*1024,
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger