import logging
from functools import wraps

class CustomFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[0;37m',
        'INFO': '\033[0;32m',
        'WARNING': '\033[0;33m',
        'ERROR': '\033[0;31m',
        'CRITICAL': '\033[0;41m',
    }
    RESET = '\033[0m'

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, self.RESET)
        record.msg = f'{log_color}{record.msg}{self.RESET}'
        return super().format(record)

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    formatter = CustomFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(f'Executed {func.__name__} in {execution_time:.4f} seconds')
        return result
    return wrapper

logger = setup_logger(__name__)