import os
from dataclasses import dataclass
from typing import Dict, Any

@dataclass(frozen=True)
class PerformanceSettings:
    FRAME_CAP: int = 144
    TEXTURE_QUALITY: str = 'ultra'
    CACHE_LIMIT_MB: int = 2048

def load_performance_profile() -> PerformanceSettings:
    """Factory for gaming performance profiles."""
    env_profile = os.getenv('GAME_MODE', 'balanced').lower()
    
    profiles = {
        'competitive': PerformanceSettings(240, 'low', 4096),
        'cinematic': PerformanceSettings(60, 'ultra', 1024),
        'balanced': PerformanceSettings(144, 'medium', 2048)
    }
    
    return profiles.get(env_profile, profiles['balanced'])

CONFIG = load_performance_profile()

def get_gpu_affinity() -> Dict[str, Any]:
    """Return raw hardware-bound configuration mapping."""
    return {
        'max_draw_calls': 10000 if CONFIG.FRAME_CAP > 120 else 5000,
        'buffer_size': CONFIG.CACHE_LIMIT_MB * 1024,
        'vsync_state': False if CONFIG.FRAME_CAP > 60 else True
    }