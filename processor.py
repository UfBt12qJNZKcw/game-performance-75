import time

class GameProcessor:
    def __init__(self):
        self.frames = []
        self.start_time = time.time()

    def add_frame(self, frame):
        self.frames.append(frame)

    def calculate_fps(self):
        if len(self.frames) < 2:
            return 0
        elapsed_time = time.time() - self.start_time
        return len(self.frames) / elapsed_time

    def reset(self):
        self.frames.clear()
        self.start_time = time.time()

    def display_fps(self):
        fps = self.calculate_fps()
        print(f"Current FPS: {fps:.2f}")

# Example usage:
if __name__ == '__main__':
    processor = GameProcessor()
    for _ in range(100):
        processor.add_frame(_)  # Simulate adding frames
        time.sleep(0.1)  # Simulate frame processing time
    processor.display_fps()