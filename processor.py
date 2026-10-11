import time
import zlib
import pickle
from typing import Any, Dict

class GameDataProcessor:
    """Compresses and serializes player session snapshots using zlib for memory efficiency."""
    def __init__(self, compression_level: int = 6):
        self.level = compression_level

    def serialize(self, data: Dict[str, Any]) -> bytes:
        payload = pickle.dumps(data)
        return zlib.compress(payload, level=self.level)

    def deserialize(self, blob: bytes) -> Dict[str, Any]:
        decompressed = zlib.decompress(blob)
        return pickle.loads(decompressed)

    def batch_process(self, datasets: list) -> list:
        return [self.serialize(d) for d in datasets]

def get_session_id(player_id: str) -> str:
    return f"srv_{int(time.time())}_{player_id}"

def sanitize_metrics(data: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in data.items() if isinstance(v, (int, float))}

if __name__ == '__main__':
    proc = GameDataProcessor()
    test_data = {'hp': 100, 'ammo': 30, 'pos': (12, 45, 0)}
    blob = proc.serialize(test_data)
    print(f'Compressed size: {len(blob)} bytes')