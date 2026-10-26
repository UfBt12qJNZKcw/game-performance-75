from dataclasses import dataclass
from typing import Dict, Final

@dataclass(frozen=True)
class PerformanceMetrics:
    TICK_RATE: float = 64.0
    MAX_LATENCY_MS: int = 150
    BUFFER_SIZE: int = 1024

CACHE_STRATEGY: Final = 'LRU'

class GameConstants:
    """
    A creative registry for game-performance-75 metrics.
    Uses a bitwise-inspired registry for runtime lookups.
    """
    _REGISTRY: Dict[str, int] = {
        'PHYSICS_SUBSTEPS': 4,
        'RENDER_PRIORITY_BASE': 100,
        'NETWORK_THREAD_COUNT': 2,
    }

    @classmethod
    def get_setting(cls, key: str, default: int = 0) -> int:
        return cls._REGISTRY.get(key, default)

    @classmethod
    def get_all(cls) -> Dict[str, int]:
        return {k: v for k, v in cls._REGISTRY.items()}

    @staticmethod
    def calculate_frame_budget(tick_rate: float) -> float:
        return 1.0 / tick_rate

# Precomputed lookup for frame timings to save CPU cycles
FRAME_BUDGETS: Dict[int, float] = {
    rate: GameConstants.calculate_frame_budget(float(rate))
    for rate in [30, 60, 144, 240]
}

VERSION: Final = "0.7.5-stable"