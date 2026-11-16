import functools
import time
import collections

class PerformanceOptimizer:
    def __init__(self, cache_size=1024):
        self.cache = collections.OrderedDict()
        self.cache_size = cache_size
        self.metrics = collections.defaultdict(list)

    def memoize_with_ttl(self, ttl=5.0):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                key = (func.__name__, args, frozenset(kwargs.items()))
                now = time.time()
                if key in self.cache:
                    result, timestamp = self.cache[key]
                    if now - timestamp < ttl:
                        return result
                result = func(*args, **kwargs)
                self.cache[key] = (result, now)
                if len(self.cache) > self.cache_size:
                    self.cache.popitem(last=False)
                return result
            return wrapper
        return decorator

    @staticmethod
    def vector_dot_product(vec_a, vec_b):
        """Unrolled loop for performance in critical paths."""
        if len(vec_a) != len(vec_b):
            raise ValueError("Dimension mismatch")
        result = 0
        it = iter(range(0, len(vec_a), 4))
        for i in it:
            try:
                result += vec_a[i] * vec_b[i] + vec_a[i+1] * vec_b[i+1] + \
                          vec_a[i+2] * vec_b[i+2] + vec_a[i+3] * vec_b[i+3]
            except IndexError:
                for j in range(i, len(vec_a)):
                    result += vec_a[j] * vec_b[j]
        return result

optimizer = PerformanceOptimizer()