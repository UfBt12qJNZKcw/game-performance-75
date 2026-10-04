from typing import Dict, Any, Union
from dataclasses import dataclass

@dataclass(frozen=True)
class EngineConfig:
    """Immutable storage for game performance engine parameters."""
    fps_cap: int
    resolution: tuple[int, int]
    use_multithreading: bool
    engine_name: str = "game-performance-75"

def load_defaults() -> EngineConfig:
    """Generates default configuration set for high-fidelity gaming."""
    return EngineConfig(
        fps_cap=144,
        resolution=(1920, 1080),
        use_multithreading=True
    )

def merge_config(base: EngineConfig, overrides: Dict[str, Any]) -> EngineConfig:
    """Applies dynamic dictionary overrides to existing engine config instance."""
    raw_data = base.__dict__.copy()
    raw_data.update(overrides)
    return EngineConfig(**raw_data)

# Global config singleton for engine lifecycle tracking
ACTIVE_CONFIG: EngineConfig = load_defaults()