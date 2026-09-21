import logging
import functools

# Configure logger for game-performance-75
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [PERF] - %(message)s')
logger = logging.getLogger('game_perf')

def validate_input_frame(func):
    """Decorator that treats invalid data as a performance hitch."""
    @functools.wraps(func)
    def wrapper(data, *args, **kwargs):
        if not isinstance(data, dict) or 'frame_id' not in data:
            logger.warning(f"Dropped malformed telemetry packet: {type(data).__name__}")
            return None
        if data.get('delta', 0) < 0:
            logger.error("Negative delta detected: possible system clock drift")
            return None
        return func(data, *args, **kwargs)
    return wrapper

@validate_input_frame
def process_telemetry(data):
    """Simulated main loop processing unit."""
    logger.info(f"Processing frame {data['frame_id']} at {data['delta']}ms")
    return True

# Mocking input loop
if __name__ == '__main__':
    inputs = [
        {'frame_id': 1, 'delta': 16.6},
        {'corrupt': 'data'},
        {'frame_id': 2, 'delta': -1},
        {'frame_id': 3, 'delta': 8.3}
    ]
    for i in inputs:
        process_telemetry(i)