import os
import functools

class PerformanceConfig:
    __slots__ = ('cache_size', 'priority_mode', 'lazy_load')
    
    def __init__(self):
        self.cache_size = int(os.getenv('CACHE_SIZE', 1024))
        self.priority_mode = os.getenv('PRIORITY', 'balanced') == 'high'
        self.lazy_load = True

    @staticmethod
    def memoize_heavy_calc(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
            if args not in cache:
                if len(cache) > 500:
                    cache.clear()
                cache[args] = func(*args)
            return cache[args]
        return wrapper

@functools.lru_cache(maxsize=128)
def get_game_settings(context_id):
    # Simulated high-frequency configuration fetch
    base = {'fps_cap': 144, 'v_sync': False, 'shadow_res': 2048}
    if context_id == 'low_power':
        base.update({'fps_cap': 60, 'shadow_res': 1024})
    return base

def hot_reload_config():
    return PerformanceConfig()

GLOBAL_CONFIG = hot_reload_config()