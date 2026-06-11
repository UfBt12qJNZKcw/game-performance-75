import logging
from logging.handlers import RotatingFileHandler

# Logger setup function

def setup_logger(logger_name, log_file, level=logging.INFO):
    handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=10)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Example of using the logger setup
def main():
    my_logger = setup_logger('game_logger', 'game_performance.log')
    my_logger.info('Starting the game performance logging')
    my_logger.warning('This is a warning message')

if __name__ == '__main__':
    main()