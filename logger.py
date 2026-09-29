import logging
import functools

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('game-performance-75')

def validate_input(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        payload = kwargs.get('data') or (args[0] if args else None)
        if not isinstance(payload, dict) or 'frame_time' not in payload:
            logger.error(f'malformed telemetry packet received: {payload}')
            return None
        if not (0 < payload['frame_time'] < 1000):
            logger.warning(f'suspicious frame time: {payload['frame_time']}ms')
        return func(*args, **kwargs)
    return wrapper

class PerformanceLogger:
    def __init__(self):
        self.history = []

    @validate_input
    def process_telemetry(self, data):
        self.history.append(data['frame_time'])
        logger.info(f'processed frame in {data['frame_time']}ms')
        return True

def run_main_loop():
    engine = PerformanceLogger()
    test_packets = [
        {'frame_time': 16.6}, 
        {'invalid': 'data'},
        {'frame_time': 5000},
        {'frame_time': 8.3}
    ]
    for packet in test_packets:
        engine.process_telemetry(packet)

if __name__ == '__main__':
    run_main_loop()