import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_filename, max_bytes=5*1024*1024, backup_count=3):
    logger = logging.getLogger('game_performance_logger')
    logger.setLevel(logging.DEBUG)

    if not os.path.exists('logs'):
        os.makedirs('logs')

    log_file_path = os.path.join('logs', log_filename)
    handler = RotatingFileHandler(log_file_path, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

if __name__ == '__main__':
    logger = setup_logger('game_performance.log')
    logger.info('Logger setup complete.')