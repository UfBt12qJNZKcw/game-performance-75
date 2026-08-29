import functools
import hashlib
from collections import deque

class PerformanceValidators:
    def __init__(self, max_cache=256):
        self.max_cache = max_cache
        self.cache = {}
        self.order = deque()

    def _generate_key(self, metrics):
        sorted_items = tuple(sorted(metrics.items()))
        return hashlib.md5(str(sorted_items).encode()).hexdigest()

    @functools.lru_cache(maxsize=128)
    def validate_fps(self, fps):
        return fps >= 30 and fps <= 144

    def validate_performance(self, metrics):
        key = self._generate_key(metrics)
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]

        fps_valid = self.validate_fps(metrics.get('fps', 0))
        lat_valid = metrics.get('latency', 999) <= 16
        mem_valid = metrics.get('memory', 100) < 80

        combined = (int(fps_valid) << 2) + (int(lat_valid) << 1) + int(mem_valid)
        is_good = combined == 7

        self.cache[key] = is_good
        self.order.append(key)

        if len(self.cache) > self.max_cache:
            oldest = self.order.popleft()
            if oldest in self.cache:
                del self.cache[oldest]

        return is_good

    def validate_batch(self, batch_metrics):
        validated = []
        good_count = 0
        for m in batch_metrics:
            res = self.validate_performance(m)
            validated.append(res)
            if res:
                good_count += 1
        avg_perf = good_count / len(validated) if validated else 0
        return {'results': validated, 'average_good': avg_perf}