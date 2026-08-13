import time
from functools import wraps

# Performance optimization decorator

def profile(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f'Function {func.__name__} executed in {end_time - start_time:.4f} seconds')
        return result
    return wrapper

class GameEngine:
    def __init__(self, name):
        self.name = name
        self.frame_rate = 60

    @profile
    def run(self):
        print(f'Running {self.name} at {self.frame_rate} FPS')
        # Main game loop simulation
        for _ in range(3):  # Simulate some processing
            time.sleep(0.2)

    @profile
    def load_assets(self, assets):
        print(f'Loading assets: {assets}')
        # Simulate asset loading
        time.sleep(len(assets) * 0.1)

if __name__ == '__main__':
    game_engine = GameEngine('EpicGame')
    game_engine.load_assets(['sprite1.png', 'sprite2.png', 'level1.map'])
    game_engine.run()