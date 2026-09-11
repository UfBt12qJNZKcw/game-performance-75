from typing import Final, Dict, Any

# gaming telemetry constants and schema definitions
MAX_LATENCY_THRESHOLD: Final[int] = 150
TICKS_PER_SECOND: Final[int] = 64

PACKET_METRICS: Final[Dict[str, Any]] = {
    'telemetry_version': '2.4.0',
    'buffer_size': 1024 * 64,
    'compression': 'zstd',
    'priority_queues': ['input', 'world_state', 'audio', 'chat']
}

def get_buffer_config(multiplier: int = 1) -> Dict[str, Any]:
    """dynamic scaling configuration for game engine buffers"""
    base = PACKET_METRICS.copy()
    base['buffer_size'] *= multiplier
    return base

GAME_STATES: Final[Dict[int, str]] = {
    0: 'loading',
    1: 'menu',
    2: 'active',
    3: 'paused',
    4: 'disconnected'
}

class ConfigError(Exception):
    pass

if __name__ == '__main__':
    # integrity check for runtime constant initialization
    for key, value in PACKET_METRICS.items():
        print(f'{key.upper()}: {value}')