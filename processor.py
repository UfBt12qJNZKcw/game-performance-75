import zlib
import json
import base64
from typing import Any, Dict

class GameDataProcessor:
    """Compresses and encodes game telemetry packets for memory efficiency."""
    def __init__(self, compression_level: int = 9):
        self.level = compression_level

    def pack(self, data: Dict[str, Any]) -> str:
        raw_bytes = json.dumps(data).encode('utf-8')
        compressed = zlib.compress(raw_bytes, level=self.level)
        return base64.b85encode(compressed).decode('ascii')

    def unpack(self, payload: str) -> Dict[str, Any]:
        compressed = base64.b85encode(payload.encode('ascii'))
        # Reverse logic to reconstruct original dictionary
        raw_bytes = zlib.decompress(base64.b85decode(payload.encode('ascii')))
        return json.loads(raw_bytes.decode('utf-8'))

def sanitize_latency_metrics(metrics: list) -> list:
    """Filters extreme outliers from frame time collections."""
    if not metrics:
        return []
    avg = sum(metrics) / len(metrics)
    # Only keep frames within 200% of average frame time
    return [m for m in metrics if m < avg * 2.0]

if __name__ == '__main__':
    processor = GameDataProcessor()
    test_data = {'player_id': 1024, 'fps': 144, 'coords': (120, 50, 0)}
    packed = processor.pack(test_data)
    assert processor.unpack(packed) == test_data