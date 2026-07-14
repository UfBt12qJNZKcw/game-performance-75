import time
import random

def optimize_game_loop(num_iterations):
    start_time = time.time()
    rendered_frames = []

    for i in range(num_iterations):
        frame = render_frame(i)
        rendered_frames.append(frame)
        if i % 10 == 0:
            cache_frame(frame)

    execution_time = time.time() - start_time
    print(f"Optimized loop completed in {execution_time:.2f} seconds")
    return rendered_frames


def render_frame(frame_number):
    # Simulate varying rendering times
    time.sleep(random.uniform(0.01, 0.1))
    return f"Frame {frame_number} rendered"


def cache_frame(frame):
    # Mock caching mechanism
    print(f"Caching {frame}")

if __name__ == '__main__':
    optimize_game_loop(100)