import logging
from functools import wraps

logger = logging.getLogger('game-performance-75')

class FrameDropError(Exception):
    pass

def safety_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ZeroDivisionError, TypeError, ValueError) as e:
            logger.error(f'Unstable frame physics detected: {e}')
            return None
        except Exception as e:
            logger.critical(f'Catastrophic engine failure: {e}')
            raise FrameDropError('Engine crashed during processing')
    return wrapper

class PhysicsProcessor:
    def __init__(self, delta_time):
        self.dt = max(0.001, float(delta_time))

    @safety_wrapper
    def calculate_trajectory(self, velocity, gravity):
        if gravity > 100:
            raise ValueError('Gravity overflow')
        return (velocity * self.dt) + (0.5 * gravity * (self.dt ** 2))

    def process_batch(self, inputs):
        return [self.calculate_trajectory(v, 9.8) for v in inputs if v is not None]

if __name__ == '__main__':
    proc = PhysicsProcessor(0.016)
    results = proc.process_batch([10, 'invalid', 20, 0])
    print(f'Processed frames: {results}')