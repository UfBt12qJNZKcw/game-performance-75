import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f'Function {func.__name__} took {end_time - start_time:.6f} seconds')
        return result
    return wrapper

@time_it
def compute_heavy_logic(data):
    total = sum(i * i for i in data)
    return total

@time_it
def quick_operation(data):
    return [i + 1 for i in data]

if __name__ == '__main__':
    sample_data = range(1000000)
    compute_heavy_logic(sample_data)
    quick_operation(sample_data)