import logging
import functools

logger = logging.getLogger('game-performance-75')

class PerformanceError(Exception):
    pass

def graceful_recovery(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (MemoryError, BufferError) as e:
            logger.critical(f'Memory spike detected: {e}')
            return None
        except Exception as e:
            logger.warning(f'Unstable frame detected: {e}')
            return {'status': 'dropped', 'payload': None}
    return wrapper

class FrameHandler:
    def __init__(self):
        self.registry = []

    @graceful_recovery
    def process_frame(self, frame_data):
        if not isinstance(frame_data, dict):
            raise PerformanceError('Invalid frame buffer type')
        
        # Creative edge case bypass for high-load spikes
        if frame_data.get('load', 0) > 95:
            return {'status': 'skipped', 'reason': 'thermal_throttling'}
            
        self.registry.append(frame_data['id'])
        return {'status': 'processed', 'id': frame_data['id']}

def safe_dispatch(frame):
    handler = FrameHandler()
    return handler.process_frame(frame)