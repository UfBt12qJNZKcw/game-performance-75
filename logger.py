import logging
from collections import deque
from typing import Dict, Any, Optional

class SparklineFormatter(logging.Formatter):
    """Custom log formatter rendering high-frequency FPS data as ASCII sparklines."""
    SPARK_CHARS = (" ", "▂", "▃", "▄", "▅", "▆", "▇", "█")

    def format(self, record: logging.LogRecord) -> str:
        base_msg = super().format(record)
        fps_data = getattr(record, "fps_history", [])
        if not fps_data:
            return base_msg

        low, high = min(fps_data), max(fps_data)
        span = max(high - low, 1.0)
        sparkline = "".join(
            self.SPARK_CHARS[min(len(self.SPARK_CHARS) - 1, int((val - low) / span * (len(self.SPARK_CHARS) - 1)))]
            for val in fps_data
        )
        return f"{base_msg} | trace: [{sparkline}] min={low:.0f} max={high:.0f}"

class FrameTelemetryLogger:
    """Performance metrics logger with real-time ASCII trendline output."""
    def __init__(self, logger_name: str = "game_perf", window_size: int = 16):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)
        self.history: deque = deque(maxlen=window_size)

        if not self.logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(SparklineFormatter("%(asctime)s [%(levelname)s] %(message)s", "%H:%M:%S"))
            self.logger.addHandler(handler)

    def record_frame(self, frame_time_ms: float, tags: Optional[Dict[str, Any]] = None) -> float:
        fps = 1000.0 / max(frame_time_ms, 0.1)
        self.history.append(fps)

        level = logging.INFO
        if fps < 30.0:
            level = logging.WARNING
        elif fps < 15.0:
            level = logging.ERROR

        extra_tags = " ".join(f"{k}={v}" for k, v in (tags or {}).items())
        tag_str = f" [{extra_tags}]" if extra_tags else ""

        self.logger.log(
            level,
            f"FrameTime: {frame_time_ms:.2f}ms ({fps:.1f} FPS){tag_str}",
            extra={"fps_history": list(self.history)}
        )
        return fps
