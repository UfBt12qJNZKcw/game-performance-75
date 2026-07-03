import numpy as np

class GameProcessor:
    def __init__(self, game_data):
        self.game_data = game_data
        self.processed_data = []

    def normalize_data(self):
        max_val = np.max(self.game_data)
        min_val = np.min(self.game_data)
        range_val = max_val - min_val
        self.processed_data = [(x - min_val) / range_val for x in self.game_data]

    def analyze_performance(self):
        mean_value = np.mean(self.processed_data)
        return {'mean_performance': mean_value, 'max_performance': np.max(self.processed_data)}

    def display_summary(self):
        self.normalize_data()
        performance = self.analyze_performance()
        print(f"Mean Performance: {performance['mean_performance']:.2f}")
        print(f"Max Performance: {performance['max_performance']:.2f}")

# Example usage:
if __name__ == '__main__':
    raw_game_data = [100, 200, 150, 300, 250]
    processor = GameProcessor(raw_game_data)
    processor.display_summary()
