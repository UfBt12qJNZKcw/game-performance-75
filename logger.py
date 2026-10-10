import os
import logging
from logging.handlers import RotatingFileHandler
from typing import Optional

class GameTelemetryFormatter(logging.Formatter):
    """Custom formatter for rendering frame telemetry and severity icons."""
    
    LEVEL_ICONS = {
        logging.DEBUG: "🎮 [TRACE]",
        logging.INFO: "⚡ [PERF]",
        logging.WARNING: "⚠️ [LAG]",
        logging.ERROR: "💥 [DROP]",
        logging.CRITICAL: "🔥 [STALL]"
    }

    def format(self, record: logging.LogRecord) -> str:
        icon = self.LEVEL_ICONS.get(record.levelno, "[GAME]")
        fps = getattr(record, "fps", "--")
        frame_ms = getattr(record, "frame_ms", "--")
        base_msg = super().format(record)
        return f"{icon} (FPS: {fps} | {frame_ms}ms) {base_msg}"

def setup_game_logger(
    log_file: str = "logs/game_telemetry.log",
    max_bytes: int = 2 * 1024 * 1024,
    backup_count: int = 5,
    level: int = logging.INFO
) -> logging.Logger:
    """Configures a rotating performance logger tailored for game metrics."""
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    logger = logging.getLogger("game_performance")
    logger.setLevel(level)
    logger.handlers.clear()

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_fmt = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S"
    )
    file_handler.setFormatter(file_fmt)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(GameTelemetryFormatter("%(message)s"))

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    
    return logger

def log_frame_spike(logger: logging.Logger, fps: float, frame_ms: float, detail: str) -> None:
    """Logs low FPS or frame timing budget overruns."""
    extra = {"fps": f"{fps:.1f}", "frame_ms": f"{frame_ms:.2f}"}
    if fps < 30.0 or frame_ms > 33.3:
        logger.warning(f"Frame budget overrun: {detail}", extra=extra)
    else:
        logger.info(f"Frame timing stable: {detail}", extra=extra)
