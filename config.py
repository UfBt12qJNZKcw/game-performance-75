import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler('app.log', maxBytes=10*1024*1024, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

if __name__ == '__main__':
    my_logger = setup_logger('my_game_logger')
    my_logger.debug('This is a debug message')
    my_logger.info('Informational message here')
    my_logger.warning('Warning message')
    my_logger.error('An error occurred')
    my_logger.critical('Critical issue!')
