import functools
import time

class HotCache:
    def __init__(self, capacity=128):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in self.cache:
                self.order.remove(key)
                self.order.append(key)
                return self.cache[key]
            result = func(*args, **kwargs)
            if len(self.cache) >= self.capacity:
                del self.cache[self.order.pop(0)]
            self.cache[key] = result
            self.order.append(key)
            return result
        return wrapper

@HotCache(capacity=256)
def calculate_frame_geometry(vertex_data, matrix):
    transformed = []
    for v in vertex_data:
        x = v[0] * matrix[0] + v[1] * matrix[1] + matrix[2]
        y = v[0] * matrix[3] + v[1] * matrix[4] + matrix[5]
        transformed.append((x, y))
    return transformed

def fast_batch_process(data_stream, processor_func):
    return [processor_func(item) for item in data_stream]

if __name__ == '__main__':
    pass