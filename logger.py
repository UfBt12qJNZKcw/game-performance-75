import logging
import os
import sys
from logging.handlers import RotatingFileHandler

class FramePerformanceFormatter(logging.Formatter):
    """Custom formatter highlighting FPS drops and render tick telemetry."""
    
    COLORS = {
        'DEBUG': '\033[94m',
        'INFO': '\033[92m',
        'WARNING': '\033[93m',
        'ERROR': '\033[91m',
        'CRITICAL': '\033[95m',
        'RESET': '\033[0m'
    }

    def format(self, record):
        fps = getattr(record, 'fps', None)
        fps_str = f" [FPS: {fps:.1f}]" if fps is not None else " [FPS: ---]"
        color = self.COLORS.get(record.levelname, self.COLORS['RESET'])
        reset = self.COLORS['RESET']
        
        timestamp = self.formatTime(record, "%H:%M:%S.%f")[:-3]
        record.msg = f"{color}[{timestamp}]{fps_str} {record.getMessage()}{reset}"
        return record.msg

class FrameAwareRotatingHandler(RotatingFileHandler):
    """Rotates log files based on file size or frame-tick thresholds."""
    
    def __init__(self, filename, maxBytes=2097152, backupCount=5, frame_interval=10000):
        super().__init__(filename, maxBytes=maxBytes, backupCount=backupCount)
        self.frame_interval = frame_interval
        self._frame_count = 0

    def emit(self, record):
        if getattr(record, 'fps', None) is not None:
            self._frame_count += 1
            if self._frame_count >= self.frame_interval:
                self._frame_count = 0
                self.doRollover()
        super().emit(record)

def setup_game_logger(name="game_perf", log_file="telemetry.log", max_mb=5, frame_rotation_interval=20000):
    """Configures a telemetry logger with frame-count and byte-limit log rotation."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    file_handler = FrameAwareRotatingHandler(
        log_file, 
        maxBytes=max_mb * 1024 * 1024, 
        backupCount=4, 
        frame_interval=frame_rotation_interval
    )
    file_handler.setFormatter(FramePerformanceFormatter())
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FramePerformanceFormatter())
    logger.addHandler(console_handler)

    return logger
