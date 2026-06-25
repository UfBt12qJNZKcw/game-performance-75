import logging

class Logger:
    def __init__(self, name, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        if not self.logger.handlers:
            ch = logging.StreamHandler()
            ch.setLevel(level)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)

    def log(self, message, level=logging.INFO):
        try:
            if not isinstance(message, str):
                raise ValueError('Message must be a string.')
            if level not in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]:
                raise ValueError('Invalid logging level.')
            self.logger.log(level, message)
        except ValueError as ve:
            self.logger.error(f'ValueError: {ve}')
        except Exception as e:
            self.logger.error(f'Unexpected exception: {e}')

if __name__ == '__main__':
    log = Logger('GameLogger')
    log.log('Game started successfully!')
    log.log('An error occurred: %s', 404, level=logging.ERROR)
