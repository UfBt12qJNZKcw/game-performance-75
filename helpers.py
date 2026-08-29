import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

class GamePerformanceLogger:
    def __init__(self, name: str = "game-performance-75"):
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self.metrics = []
        self._configure_rotating_handlers()

    def _configure_rotating_handlers(self):
        log_dir = Path("game_logs")
        log_dir.mkdir(exist_ok=True)
        log_file = log_dir / f"{self.name}.log"
        handler = RotatingFileHandler(
            log_file, maxBytes=10485760, backupCount=5
        )
        handler.setFormatter(logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s"
        ))
        self.logger.addHandler(handler)

    def log(self, message: str, level: str = "info"):
        log_func = getattr(self.logger, level, self.logger.info)
        log_func(message)
        if level == "info":
            self.metrics.append(message)
            if len(self.metrics) > 200:
                self.metrics.pop(0)

    def get_recent_metrics(self):
        return self.metrics[:]

def setup_logger():
    return GamePerformanceLogger()