import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file, max_bytes=10*1024*1024, backup_count=5):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

if __name__ == '__main__':
    log = setup_logger('game_log.log')
    log.info('Logger setup complete')
    log.error('This is an error message')
    log.debug('This is a debug message')