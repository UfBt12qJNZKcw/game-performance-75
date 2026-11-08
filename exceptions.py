import time
from typing import Any, Dict, Optional


class GamePerformanceError(Exception):
    """Base exception class capturing real-time telemetry metadata."""

    def __init__(
        self,
        message: str,
        fps: Optional[float] = None,
        frametime_ms: Optional[float] = None,
        severity: int = 1,
    ):
        self.timestamp = time.perf_counter()
        self.fps = fps
        self.frametime_ms = frametime_ms
        self.severity = min(max(severity, 1), 5)
        self.telemetry_snapshot = self._capture_context()
        super().__init__(self._format_message(message))

    def _capture_context(self) -> Dict[str, Any]:
        delta = (1000.0 / self.fps - 16.67) if self.fps and self.fps > 0 else 0.0
        return {
            "epoch_ns": time.time_ns(),
            "target_fps": 60.0,
            "delta_deviation_ms": round(delta, 3),
        }

    def _format_message(self, msg: str) -> str:
        metrics = []
        if self.fps is not None:
            metrics.append(f"FPS={self.fps:.1f}")
        if self.frametime_ms is not None:
            metrics.append(f"Frametime={self.frametime_ms:.2f}ms")
        metrics_str = f" [{', '.join(metrics)}]" if metrics else ""
        return f"[SEV-{self.severity}] {msg}{metrics_str}"


class FrameDropError(GamePerformanceError):
    """Raised when continuous frame drops violate smooth rendering threshold."""

    def __init__(self, dropped_frames: int, actual_fps: float):
        self.dropped_frames = dropped_frames
        frametime = (1000.0 / actual_fps) if actual_fps > 0 else 999.0
        msg = f"Dropped {dropped_frames} consecutive frames"
        super().__init__(msg, fps=actual_fps, frametime_ms=frametime, severity=3)


class GPUThrottlingError(GamePerformanceError):
    """Raised when GPU thermal limits degrade frame cadence."""

    def __init__(self, temp_celsius: float, core_clock_mhz: int):
        self.temp_celsius = temp_celsius
        self.core_clock_mhz = core_clock_mhz
        msg = f"GPU throttle trigger at {temp_celsius}°C ({core_clock_mhz} MHz)"
        super().__init__(msg, severity=5)


class RenderPipelineStall(GamePerformanceError):
    """Raised when render thread waiting exceeds budget allocation."""

    def __init__(self, stall_duration_ms: float, stage_name: str):
        self.stall_duration_ms = stall_duration_ms
        self.stage_name = stage_name
        msg = f"Pipeline stall in '{stage_name}' lasting {stall_duration_ms:.2f}ms"
        super().__init__(msg, frametime_ms=stall_duration_ms, severity=4)
