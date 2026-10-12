import logging

class PerformanceOptimizer:
    def __init__(self):
        self.logger = logging.getLogger('game-performance-75')

    def process_frame_data(self, data: dict):
        try:
            if not isinstance(data, dict):
                raise ValueError('invalid input payload format')
            
            fps = data.get('fps')
            if fps is None:
                return 0
            
            if fps < 0 or fps > 999:
                raise ValueError(f'out of range fps value: {fps}')
                
            return int(fps) * 1.5
        except (ValueError, TypeError) as e:
            self.logger.error(f'optimization anomaly: {e}')
            return 0
        except Exception as e:
            self.logger.critical(f'unexpected system collapse: {e}')
            return -1

    def validate_batch(self, batch):
        if not batch:
            return []
        
        results = []
        for item in batch:
            processed = self.process_frame_data(item)
            if processed != -1:
                results.append(processed)
            else:
                self.logger.warning('skipping malformed frame chunk')
        return results