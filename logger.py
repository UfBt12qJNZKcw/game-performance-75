import sys
import time
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

class GameFrameFormatter(logging.Formatter):
    """Custom formatter injecting uptime and FPS performance markers into logs."""
    def __init__(self, fmt: str = None, datefmt: str = None):
        super().__init__(fmt, datefmt)
        self._start_time = time.monotonic()

    def format(self, record: logging.LogRecord) -> str:
        uptime = time.monotonic() - self._start_time
        record.uptime = f"{uptime:08.3f}s"
        if not hasattr(record, "fps"):
            record.fps = "--"
        return super().format(record)

def setup_telemetry_logger(
    name: str = "game_perf",
    log_dir: str = "logs",
    max_bytes: int = 1_048_576,
    backup_count: int = 5
) -> logging.Logger:
    """Configures a rotating log facility tailored for real-time telemetry output."""
    target_dir = Path(log_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    log_file = target_dir / f"{name}.log"

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    log_fmt = "[%(asctime)s] [%(uptime)s] [%(levelname)s] [FPS: %(fps)s] %(message)s"
    formatter = GameFrameFormatter(fmt=log_fmt, datefmt="%H:%M:%S")

    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger

perf_logger = setup_telemetry_logger()
