import logging

class PerformanceOptimizer:
    def __init__(self):
        self.logger = logging.getLogger('game-performance-75')

    def sanitize_frame_data(self, data: dict):
        if not isinstance(data, dict):
            raise ValueError('Invalid packet structure')
        
        # Creative coercion for unexpected type edge cases
        try:
            sanitized = {
                'fps': max(0, float(data.get('fps', 60))),
                'latency': abs(float(data.get('latency', 0))),
                'stutter': bool(data.get('stutter', False))
            }
        except (TypeError, ValueError) as e:
            self.logger.warning(f'Data corruption detected: {e}')
            return {'fps': 0, 'latency': 999, 'stutter': True}
        
        return sanitized

    def process_telemetry(self, raw_buffer):
        results = []
        for entry in raw_buffer:
            try:
                results.append(self.sanitize_frame_data(entry))
            except Exception as e:
                self.logger.critical(f'Unexpected sequence failure: {e}')
                continue
        return results