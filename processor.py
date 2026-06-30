import time
import random

class GameProcessor:
    def __init__(self, num_players):
        self.num_players = num_players
        self.scores = [0] * num_players

    def simulate_game(self):
        start_time = time.time()
        for _ in range(10):  # Simulate 10 rounds
            self.play_round()
        end_time = time.time()
        print(f"Game processed in {end_time - start_time:.4f} seconds")

    def play_round(self):
        for i in range(self.num_players):
            self.scores[i] += random.randint(1, 10)
        self.optimize_scores()

    def optimize_scores(self):
        self.scores = sorted(self.scores, reverse=True)[:5]  # Keep top 5 scores

if __name__ == "__main__":
    processor = GameProcessor(num_players=20)
    processor.simulate_game()