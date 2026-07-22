import logging
from logging.handlers import RotatingFileHandler

class Logger:
    def __init__(self, name='game_performance', max_bytes=5*1024*1024, backup_count=3):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = RotatingFileHandler('game_performance.log', maxBytes=max_bytes, backupCount=backup_count)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

logger_instance = Logger()