import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='game.log', max_bytes=5 * 1024 * 1024, backup_count=3):
    logger = logging.getLogger('GameLogger')
    logger.setLevel(logging.INFO)
    
    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    
    # Add the handler to the logger
    logger.addHandler(handler)
    return logger

# Example usage
def main():
    logger = setup_logger()
    logger.info('Game started')
    logger.warning('This is a warning')
    logger.error('An error occurred')

if __name__ == '__main__':
    main()