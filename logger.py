import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

class PerformanceLogger:
    def __init__(self, name: str = 'game_perf'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        log_dir = Path('logs')
        log_dir.mkdir(exist_ok=True)
        
        handler = RotatingFileHandler(
            log_dir / 'engine.log',
            maxBytes=5 * 1024 * 1024,
            backupCount=3
        )
        
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | [%(name)s] -> %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
        if not self.logger.handlers:
            console = logging.StreamHandler()
            console.setFormatter(formatter)
            self.logger.addHandler(console)

    def get_logger(self):
        return self.logger

def setup_game_logging(name: str = 'game_perf'):
    return PerformanceLogger(name).get_logger()