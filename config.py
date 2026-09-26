from typing import Dict, Any, Union
from dataclasses import dataclass

@dataclass(frozen=True)
class EngineSettings:
    """Immutable configuration container for game engine tuning parameters."""
    fps_cap: int = 144
    use_multithreading: bool = True
    buffer_size: int = 4096

def load_game_config(raw_data: Dict[str, Union[int, bool]]) -> EngineSettings:
    """Parses dictionary input into strict EngineSettings via mapping."""
    return EngineSettings(
        fps_cap=int(raw_data.get("fps_cap", 60)),
        use_multithreading=bool(raw_data.get("use_multithreading", True)),
        buffer_size=int(raw_data.get("buffer_size", 2048))
    )

def get_environment_defaults() -> Dict[str, Any]:
    """Generates default registry for runtime engine environment."""
    return {
        "gpu_acceleration": True,
        "v_sync": False,
        "shader_cache_path": "./cache/shaders"
    }

# Configuration injection for performance optimization context
GLOBAL_CONFIG: EngineSettings = EngineSettings(fps_cap=240, use_multithreading=True)