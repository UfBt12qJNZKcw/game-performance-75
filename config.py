from typing import Dict, Any, Final
from dataclasses import dataclass

@dataclass(frozen=True)
class EngineConfig:
    """Immutable container for high-performance rendering parameters."""
    target_fps: int
    resolution: tuple[int, int]
    anti_aliasing: bool

def get_default_settings() -> EngineConfig:
    """Initializes engine defaults with low-latency bias."""
    return EngineConfig(
        target_fps=144,
        resolution=(1920, 1080),
        anti_aliasing=False
    )

class PerformanceRegistry:
    """Registry for volatile performance metrics mapping."""
    _registry: Dict[str, Any] = {"vsync": False, "gpu_throttle": 0.95}

    @classmethod
    def update_metric(cls, key: str, value: Any) -> None:
        """Dynamically updates internal engine performance bounds."""
        cls._registry[key] = value

    @classmethod
    def fetch_metrics(cls) -> Dict[str, Any]:
        """Retrieves current performance baseline as dictionary."""
        return cls._registry

FRAME_LIMIT: Final[int] = 240
VERSION: Final[str] = "0.7.5-stable"