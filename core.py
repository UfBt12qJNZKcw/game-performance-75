import numpy as np

class GameData:
    def __init__(self, frame_count):
        self.frame_count = frame_count
        self.data = np.zeros((frame_count, 3), dtype=np.float32)  # Store position, speed, and time

    def update_frame(self, frame_idx, position, speed):
        if 0 <= frame_idx < self.frame_count:
            self.data[frame_idx] = np.array([position, speed, frame_idx], dtype=np.float32)

    def process_frames(self):
        return np.mean(self.data, axis=0)

# Simulate game performance tracking
if __name__ == '__main__':
    game_data = GameData(1000)
    for i in range(1000):
        game_data.update_frame(i, np.random.random(), np.random.random())
    average_metrics = game_data.process_frames()
    print(f'Average metrics: {average_metrics}')