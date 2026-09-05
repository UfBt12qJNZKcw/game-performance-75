import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_game_logger(name: str = 'performance-75', log_dir: str = 'logs') -> logging.Logger:
    path = Path(log_dir)
    path.mkdir(exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%H:%M:%S'
    )

    file_handler = RotatingFileHandler(
        path / f'{name}.log', 
        maxBytes=2*1024*1024, 
        backupCount=5
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
    return logger

if __name__ == '__main__':
    log = setup_game_logger()
    log.info('performance tracking engine initialized')