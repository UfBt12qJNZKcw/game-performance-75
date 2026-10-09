import re
from typing import Any, Dict, List

class PerformanceValidator:
    def __init__(self, thresholds: Dict[str, float]):
        self.thresholds = thresholds
        self._pattern = re.compile(r'^([a-zA-Z_]+)_([0-9]+)$')

    def validate_metric(self, key: str, value: float) -> bool:
        if key not in self.thresholds:
            return True
        return value <= self.thresholds[key]

    def sanitize_frame_data(self, data: Dict[str, Any]) -> Dict[str, float]:
        return {k: float(v) for k, v in data.items() if isinstance(v, (int, float))}

    def batch_check(self, payload: List[Dict[str, Any]]) -> List[bool]:
        results = []
        for entry in payload:
            valid = all(self.validate_metric(k, v) for k, v in entry.items())
            results.append(valid)
        return results

class ConfigSchemaValidator:
    @staticmethod
    def enforce_limits(config: Dict[str, Any]) -> None:
        required = ['fps_cap', 'render_scale']
        for req in required:
            if req not in config:
                raise ValueError(f'missing {req} in configuration')

    @staticmethod
    def normalize_keys(data: Dict[str, Any]) -> Dict[str, Any]:
        return {k.lower().strip(): v for k, v in data.items()}