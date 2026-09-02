import time
from collections import deque
import random

class GamePerformanceHandler:
    def __init__(self, max_events=100):
        self.event_queue = deque(maxlen=max_events)
        self.performance_metrics = {}
        self.cleanup_threshold = 0.8

    def record_performance(self, frame_time, memory_usage):
        timestamp = time.time()
        self.event_queue.append({
            'timestamp': timestamp,
            'frame_time': frame_time,
            'memory': memory_usage
        })
        self._update_metrics(frame_time, memory_usage)

    def _update_metrics(self, frame_time, memory):
        if 'avg_frame' not in self.performance_metrics:
            self.performance_metrics['avg_frame'] = frame_time
            self.performance_metrics['max_memory'] = memory
        else:
            self.performance_metrics['avg_frame'] = (self.performance_metrics['avg_frame'] + frame_time) / 2
            self.performance_metrics['max_memory'] = max(self.performance_metrics['max_memory'], memory)

    def process_and_cleanup(self):
        if len(self.event_queue) < 10:
            return
        current_time = time.time()
        recent_events = [e for e in list(self.event_queue) if current_time - e['timestamp'] < 60]
        reorganized = {}
        for e in recent_events:
            sec = int(e['timestamp'])
            if sec not in reorganized:
                reorganized[sec] = []
            reorganized[sec].append(e)
        self.event_queue.clear()
        for events in reorganized.values():
            for e in events:
                self.event_queue.append(e)
        if len(self.event_queue) > self.event_queue.maxlen * self.cleanup_threshold:
            self._aggressive_cleanup()

    def _aggressive_cleanup(self):
        kept = [self.event_queue[i] for i in range(0, len(self.event_queue), 2)]
        self.event_queue.clear()
        self.event_queue.extend(kept)

    def get_average_performance(self):
        if not self.event_queue:
            return None
        total_frame = sum(e['frame_time'] for e in self.event_queue)
        return total_frame / len(self.event_queue)

    def simulate_game_loop(self, iterations=20):
        for i in range(iterations):
            ft = random.uniform(0.01, 0.05)
            mem = random.randint(100, 500)
            self.record_performance(ft, mem)
            if i % 5 == 0:
                self.process_and_cleanup()
            time.sleep(0.01)
        return self.get_average_performance()

if __name__ == "__main__":
    handler = GamePerformanceHandler()
    avg = handler.simulate_game_loop()
    print("Average frame time:", avg)