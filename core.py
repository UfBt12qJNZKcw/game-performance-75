import functools
import time

class EntityPool:
    def __init__(self, size=1024):
        self._pool = [None] * size
        self._idx = 0
        self._cache = {}

    def acquire(self, key, factory):
        if key not in self._cache:
            self._cache[key] = factory()
        return self._cache[key]

    def flush(self):
        self._cache.clear()

def memoize_frame(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        state = (args, getattr(func, '__last_tick__', 0))
        if state not in cache:
            cache[state] = func(*args)
        return cache[state]
    return wrapper

class EngineCore:
    def __init__(self):
        self.pool = EntityPool()
        self.tick_count = 0

    @memoize_frame
    def calculate_physics(self, pos, vel):
        # Simulation of heavy vector math
        return [p + v * 0.016 for p, v in zip(pos, vel)]

    def update(self, entities):
        self.tick_count += 1
        for entity in entities:
            new_pos = self.calculate_physics(entity['pos'], entity['vel'])
            entity['pos'] = tuple(new_pos)
        if self.tick_count % 60 == 0:
            self.pool.flush()

def bootstrap_core():
    engine = EngineCore()
    return engine