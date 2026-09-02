import logging
from logging.handlers import RotatingFileHandler
import sys
from pathlib import Path
from datetime import datetime
from functools import wraps

class PerformanceRotatingHandler(RotatingFileHandler):
    def doRollover(self):
        super().doRollover()
        rollover_time = datetime.now().isoformat()
        with open(self.baseFilename, 'a') as log_file:
            log_file.write(f"# Log rotated at {rollover_time} for game session\n")

def setup_logger(log_name: str = "game_performance", max_size: int = 10485760, backups: int = 5) -> logging.Logger:
    log_path = Path("logs")
    log_path.mkdir(exist_ok=True)
    logger = logging.getLogger("game-performance-75")
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        file_handler = PerformanceRotatingHandler(
            log_path / f"{log_name}.log",
            maxBytes=max_size,
            backupCount=backups
        )
        file_handler.setLevel(logging.INFO)
        file_formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.WARNING)
        console_formatter = logging.Formatter("%(levelname)s: %(message)s")
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)
    return logger

def log_performance(logger: logging.Logger, fps: float, memory_mb: int, cpu_percent: float) -> None:
    logger.info(
        f"Performance: FPS={fps:.1f} Memory={memory_mb}MB CPU={cpu_percent:.1f}%"
    )

def performance_monitor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = setup_logger()
        start_time = datetime.now()
        result = func(*args, **kwargs)
        elapsed = (datetime.now() - start_time).total_seconds() * 1000
        logger.debug(f"{func.__name__} executed in {elapsed:.2f}ms")
        return result
    return wrapper