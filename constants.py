from enum import Enum, unique

@unique
class PerformanceThresholds(Enum):
    FPS_MIN = 30
    FPS_TARGET = 60
    FRAME_TIME_MAX_MS = 16.67
    LATENCY_THRESHOLD_MS = 50

@unique
class EngineStates(Enum):
    IDLE = 0
    WARMING_UP = 1
    STRESS_TESTING = 2
    COLLECTING_TELEMETRY = 3
    SHUTDOWN_SEQUENCE = 4

SYSTEM_CONFIG = {
    'sampling_rate': 0.1,
    'buffer_size': 1024,
    'max_retries': 3,
    'log_level': 'DEBUG',
    'hardware_acceleration': True
}

RESOURCE_PATHS = {
    'logs': './data/logs',
    'profiles': './data/profiles',
    'cache': './data/tmp'
}

ERROR_MESSAGES = {
    'MEM_LEAK': 'Critical memory threshold breach detected.',
    'GPU_HANG': 'Graphics pipeline stall imminent.',
    'THROTTLING': 'Thermal throttling triggered by kernel.'
}