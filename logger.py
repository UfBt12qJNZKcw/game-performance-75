import logging
import os

class CustomLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_info(self, message):
        try:
            self.logger.info(message)
        except Exception as e:
            self.logger.error(f'Failed to log info: {e}')

    def log_warning(self, message):
        try:
            self.logger.warning(message)
        except Exception as e:
            self.logger.error(f'Failed to log warning: {e}')

    def log_error(self, message):
        try:
            self.logger.error(message)
        except Exception as e:
            self.logger.error(f'Failed to log error: {e}')

    def log_to_file(self, message, filename):
        try:
            if not os.path.isdir(os.path.dirname(filename)):
                raise ValueError('Invalid directory for log file')
            with open(filename, 'a') as file:
                file.write(f'{message}\n')
        except (IOError, ValueError) as e:
            self.logger.error(f'Failed to log to file: {e}')

# Example usage
if __name__ == '__main__':
    logger = CustomLogger('GameLogger')
    logger.log_info('Game started')
    logger.log_warning('Low memory warning')
    logger.log_error('Unexpected error occurred')
    logger.log_to_file('Game log entry', 'logs/game.log')