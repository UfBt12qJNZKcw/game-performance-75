import logging
from logging.handlers import RotatingFileHandler

class Logger:
    def __init__(self, name, log_file='app.log', max_bytes=5*1024*1024, backup_count=5):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        # Create rotating file handler
        handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger

# Usage example if needed:
# if __name__ == '__main__':
#     my_logger = Logger('MyAppLogger').get_logger()
#     my_logger.info('This is an info message')
