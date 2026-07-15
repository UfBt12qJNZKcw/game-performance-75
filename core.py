import time

def optimize_performance(data):
    start_time = time.time()
    optimized_data = set(data)  # Removing duplicates for better performance
    processed_data = []

    for item in optimized_data:
        processed_item = complex_computation(item)
        processed_data.append(processed_item)

    print(f"Processing completed in {time.time() - start_time:.4f} seconds")
    return processed_data


def complex_computation(item):
    return item ** 2 + 10 * item + 1  # Example computation simplification


def run_game_loop(data):
    while True:
        optimized_result = optimize_performance(data)
        # Further game logic and rendering would occur here
        break  # Prevent infinite looping during optimization testing

if __name__ == '__main__':
    sample_data = list(range(1000))  # Example data
    run_game_loop(sample_data)