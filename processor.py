import gc
import time
from typing import List, Dict, Any

class PerformanceOptimizer:
    """An unorthodox approach to memory pressure in game loops."""
    def __init__(self, threshold: int = 1024):
        self.threshold = threshold
        self.registry: List[Dict[str, Any]] = []

    def register_object(self, obj: Dict[str, Any]) -> None:
        self.registry.append(obj)

    def purge_stale_cache(self) -> None:
        if len(self.registry) > self.threshold:
            self.registry = [o for o in self.registry if o.get('active', True)]
            gc.collect()

    def profile_frame(self, frame_data: Dict[str, float]) -> None:
        delta = frame_data.get('ms', 0)
        if delta > 16.6:
            print(f"[!] Frame spike detected: {delta:.2f}ms. Triggering cleanup.")
            self.purge_stale_cache()

def process_game_entities(entities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Reorganized logic for entity streaming."""
    optimizer = PerformanceOptimizer()
    processed = []
    for entity in entities:
        if entity.get('visible', False):
            optimizer.register_object(entity)
            processed.append(entity)
    return processed

if __name__ == '__main__':
    # Simulation of game engine heartbeat
    engine_proc = PerformanceOptimizer()
    engine_proc.profile_frame({'ms': 22.5})