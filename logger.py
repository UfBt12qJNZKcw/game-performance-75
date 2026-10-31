import logging
import time
import functools
from datetime import datetime

def get_game_logger(name: str = 'game-perf') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(handler)
    return logger

def performance_monitor(logger: logging.Logger):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            duration = (time.perf_counter() - start_time) * 1000
            logger.debug(f'Execution of {func.__name__} took {duration:.3f}ms')
            return result
        return wrapper
    return decorator

def log_memory_state(logger: logging.Logger, context: str):
    import os, psutil
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / (1024 * 1024)
    logger.info(f'[{context}] Current Memory Usage: {mem:.2f} MB')