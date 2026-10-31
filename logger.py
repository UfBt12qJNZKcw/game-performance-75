import logging
from logging.handlers import RotatingFileHandler
import sys

class PerformanceLogger:
    _instances = {}

    def __new__(cls, name='game_perf_engine', log_file='game_perf.log'):
        if name not in cls._instances:
            logger = logging.getLogger(name)
            logger.setLevel(logging.DEBUG)
            
            formatter = logging.Formatter(
                '%(asctime)s | [%(levelname)s] | %(name)s | %(message)s',
                datefmt='%H:%M:%S'
            )

            # Rotating file handler: 5MB per file, keep 3 backups
            file_handler = RotatingFileHandler(
                log_file, maxBytes=5*1024*1024, backupCount=3
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

            # Stream to console as well for dev mode
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

            cls._instances[name] = logger
        return cls._instances[name]

# Singleton accessor for game modules
get_logger = PerformanceLogger