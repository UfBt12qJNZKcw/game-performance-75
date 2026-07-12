import numpy as np

def optimize_performance(data):
    unique_data = np.unique(data)
    processed = np.zeros(len(unique_data))
    for i, val in enumerate(unique_data):
        processed[i] = heavy_computation(val)
    return processed


def heavy_computation(value):
    result = 0
    for i in range(1, 10001):
        result += (value * i) / (i + 1)
    return result


def batch_process(data_batch):
    results = []
    for data in data_batch:
        result = optimize_performance(data)
        results.append(result)
    return results


def concurrent_process(data_batch):
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(optimize_performance, data_batch))
    return results