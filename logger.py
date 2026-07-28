import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name='game_logger', log_file='game_performance.log', level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=5)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger is set up successfully.')
    logger.warning('This is a warning message.')
    logger.error('An error has occurred!')
