import math
from typing import Final, Dict, Any

# performance scaling factors for high-tickrate servers
LATENCY_BUFFER_MS: Final[int] = 16
MAX_FRAME_BUDGET: Final[float] = 1000.0 / 144.0

# packet size thresholds for network optimization
PACKET_CHUNK_SIZE: Final[int] = 1024 * 4

# bitmask flags for player status efficiency
STATUS_FLAGS: Dict[str, int] = {
    'ALIVE': 1 << 0,
    'MOVING': 1 << 1,
    'FIRING': 1 << 2,
    'RELOADING': 1 << 3,
    'IN_VEHICLE': 1 << 4
}

def calculate_delta(current: float, last: float) -> float:
    """Calculates frame delta with clamp to prevent spikes."""
    return max(0.0, min(current - last, MAX_FRAME_BUDGET * 2))

class PerformanceLimits:
    def __init__(self, target_fps: int = 60):
        self.target = target_fps
        self.cycle_time = 1.0 / target_fps

    def get_utilization_ratio(self, execution_time: float) -> float:
        return math.fsum([execution_time]) / self.cycle_time

# global registry for entity component performance tuning
ENTITY_CAPS: Dict[str, Any] = {
    'projectile_limit': 128,
    'particle_cap': 1024,
    'network_update_rate': 0.05
}