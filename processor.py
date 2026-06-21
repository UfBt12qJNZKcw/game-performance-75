import random
import sys

class GameProcessingError(Exception):
    pass

class GameProcessor:
    def __init__(self, data):
        if not isinstance(data, list) or not data:
            raise GameProcessingError('Data must be a non-empty list.')
        self.data = data

    def process_data(self):
        try:
            processed_data = [self._perform_calculation(d) for d in self.data]
            return processed_data
        except Exception as e:
            print(f'Error during processing: {e}')
            sys.exit(1)

    def _perform_calculation(self, value):
        if not isinstance(value, (int, float)):
            raise GameProcessingError(f'Invalid data type for value: {value}')
        # Simulate potential division by zero
        divisor = random.choice([0, 1, 2, 3])
        return value / divisor if divisor != 0 else value * 2

if __name__ == '__main__':
    try:
        processor = GameProcessor([5, 10, 'a', 20])  # Intentionally including an invalid type
        results = processor.process_data()
        print(results)
    except GameProcessingError as e:
        print(f'Game processing failed: {e}')
        sys.exit(1)