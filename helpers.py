import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = 'game_perf_logger', log_file: str = 'performance.log') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(process)d | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        handler = RotatingFileHandler(
            log_file,
            maxBytes=5 * 1024 * 1024,
            backupCount=3
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)
        
    return logger

# Quick performance diagnostic injection
def log_frame_metrics(logger: logging.Logger, frame_time: float, gpu_temp: float):
    status = "STABLE" if frame_time < 16.6 else "LAGGING"
    logger.info(f"[{status}] Frame: {frame_time:.2f}ms | GPU: {gpu_temp}°C")