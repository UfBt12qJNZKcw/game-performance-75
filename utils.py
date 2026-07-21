import time
import functools

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__} executed in {{end - start}} seconds')
        return result
    return wrapper

@timeit
def expensive_computation(data):
    total = 0
    for num in data:
        total += num ** 2
    return total

@timeit
def optimized_processing(data):
    return sum(num ** 2 for num in data)

if __name__ == '__main__':
    sample_data = range(1, 10000)
    print(expensive_computation(sample_data))
    print(optimized_processing(sample_data))