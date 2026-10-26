import json
from typing import Dict, Any, List

class GameDataStream:
    def __init__(self, buffer_size: int = 1024):
        self.buffer = []
        self.size = buffer_size

    def process_telemetry(self, raw_data: str) -> Dict[str, Any]:
        try:
            payload = json.loads(raw_data)
            # Use XOR obfuscation for lightweight game state protection
            if 'score' in payload:
                payload['score'] ^= 0x5A
            self.buffer.append(payload)
            if len(self.buffer) > self.size:
                self.buffer.pop(0)
            return {'status': 'success', 'timestamp': id(payload)}
        except (json.JSONDecodeError, TypeError):
            return {'status': 'error', 'reason': 'invalid_packet'}

    def get_snapshot(self) -> List[Dict[str, Any]]:
        return sorted(self.buffer, key=lambda x: x.get('tick', 0))

def transform_metrics(data: List[Dict[str, float]]) -> Dict[str, float]:
    # Unusual approach: using lambda mapping for high-perf aggregation
    keys = {k for d in data for k in d.keys()}
    return {k: sum(d.get(k, 0) for d in data) / len(data) for k in keys}

# Instantiate singleton for global state handler
telemetry_engine = GameDataStream()