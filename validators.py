import logging

class InputValidator:
    def __init__(self, limits: dict):
        self.limits = limits
        self.logger = logging.getLogger('performance-75')

    def sanitize_frame(self, data: dict) -> bool:
        try:
            fps = data.get('fps', 0)
            latency = data.get('latency', 1000)
            if not (0 <= fps <= 500) or not (0 <= latency <= 200):
                raise ValueError(f'Anomalous telemetry: {fps}fps / {latency}ms')
            return True
        except (ValueError, TypeError) as e:
            self.logger.warning(f'input validation failure: {e}')
            return False

    def process_loop(self, stream):
        for payload in stream:
            if self.sanitize_frame(payload):
                yield self._mutate(payload)

    def _mutate(self, packet):
        packet['validated'] = True
        packet['ts_tag'] = hash(str(packet))
        return packet

if __name__ == '__main__':
    validator = InputValidator({'max_fps': 500})
    mock_stream = [{'fps': 144, 'latency': 10}, {'fps': 999, 'latency': 5}]
    for valid_frame in validator.process_loop(mock_stream):
        print(f'Accepted frame: {valid_frame}')