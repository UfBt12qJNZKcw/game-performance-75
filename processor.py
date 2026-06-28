import numpy as np

class GameProcessor:
    def __init__(self, game_data):
        self.game_data = game_data
        self.processed_data = None

    def optimize_data(self):
        data_array = np.array(self.game_data)
        self.processed_data = (data_array - np.mean(data_array)) / np.std(data_array)
        return self.processed_data

    def compute_performance_metrics(self):
        if self.processed_data is None:
            raise ValueError('Data not processed. Call optimize_data first.')
        metrics = {
            'mean_performance': np.mean(self.processed_data),
            'std_performance': np.std(self.processed_data),
            'max_performance': np.max(self.processed_data),
            'min_performance': np.min(self.processed_data),
        }
        return metrics

if __name__ == '__main__':
    sample_data = [100, 200, 150, 300, 250]
    processor = GameProcessor(sample_data)
    processor.optimize_data()
    print(processor.compute_performance_metrics())