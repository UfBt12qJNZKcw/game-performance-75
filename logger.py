import logging

class CustomLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler('game.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_debug(self, message):
        self.logger.debug(message)

    def log_exception(self, exception):
        self.logger.exception(exception)

if __name__ == '__main__':
    logger = CustomLogger(__name__)
    try:
        # Example usage, replace this with actual loop
        for i in range(5):
            if i == 2:
                raise ValueError('Intentional Error')
            logger.log_info(f'Processing item {i}')
    except Exception as e:
        logger.log_exception(e)