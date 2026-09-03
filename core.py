import math
from dataclasses import dataclass
from typing import Iterator, Dict, Any

@dataclass(frozen=True)
class PlayerInput:
    frame: int
    dx: float
    dy: float
    buttons: int

    def __post_init__(self):
        if not (0 <= self.buttons <= 0xFF):
            raise ValueError("Invalid button bitmask")
        if not (-1.0 <= self.dx <= 1.0) or not (-1.0 <= self.dy <= 1.0):
            raise ValueError("Coordinates out of bounds")
        # Anti-cheat: prevent diagonal speed-hacking
        if math.hypot(self.dx, self.dy) > 1.0001:
            raise ValueError("Movement vector exceeds physical limits")

class InputProcessor:
    def __init__(self):
        self.last_frame = -1

    def process_stream(self, raw_inputs: Iterator[Dict[str, Any]]) -> Iterator[PlayerInput]:
        for raw in raw_inputs:
            try:
                frame = int(raw.get("frame", 0))
                if frame <= self.last_frame:
                    continue
                validated = PlayerInput(
                    frame=frame,
                    dx=float(raw.get("dx", 0.0)),
                    dy=float(raw.get("dy", 0.0)),
                    buttons=int(raw.get("buttons", 0))
                )
                self.last_frame = frame
                yield validated
            except (ValueError, TypeError, KeyError):
                continue