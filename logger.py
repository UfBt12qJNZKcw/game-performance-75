import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='game.log', max_bytes=5 * 1024 * 1024, backup_count=3):
    logger = logging.getLogger('GameLogger')
    logger.setLevel(logging.DEBUG)

    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger

# Example usage
if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger initialized successfully!')
    log.debug('This is a debug message.')
    log.warning('This is a warning message.')