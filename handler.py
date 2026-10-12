import time
from typing import Dict, Any, Optional, Callable

class FrameRateGovernor:
    """Manages game frame pacing with nanosecond precision."""

    def __init__(self, target_fps: int = 60) -> None:
        self.interval: float = 1.0 / target_fps
        self.last_frame_time: float = time.perf_counter()

    def wait(self) -> None:
        """Executes a spin-lock delay to ensure consistent frame timing."""
        next_frame_target: float = self.last_frame_time + self.interval
        while time.perf_counter() < next_frame_target:
            pass
        self.last_frame_time = time.perf_counter()

class EventStreamHandler:
    """Handles asynchronous game events with payload injection."""

    def __init__(self) -> None:
        self._subscribers: Dict[str, Callable[[Any], None]] = {}

    def subscribe(self, event_type: str, callback: Callable[[Any], None]) -> None:
        """Registers a listener for specific game state changes."""
        self._subscribers[event_type] = callback

    def emit(self, event_type: str, data: Optional[Any] = None) -> None:
        """Triggers a callback associated with an event type."""
        if event_type in self._subscribers:
            self._subscribers[event_type](data)

def initialize_game_loop(fps: int = 144) -> None:
    """Entry point for performance-critical main loop initialization."""
    governor = FrameRateGovernor(target_fps=fps)
    handler = EventStreamHandler()

    def tick() -> None:
        governor.wait()
        handler.emit("frame_render", {"ts": time.time()})

    for _ in range(100):
        tick()