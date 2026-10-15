import logging
import functools

class GamePerformanceError(Exception):
    pass

def safety_net(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ZeroDivisionError, TypeError, ValueError) as e:
            logging.error(f"Anomaly detected in {func.__name__}: {e}")
            return None
        except Exception as e:
            raise GamePerformanceError(f"Critical core collapse: {e}") from e
    return wrapper

class PerformanceHandler:
    def __init__(self, throttle_threshold=0.01):
        self.threshold = throttle_threshold

    @safety_net
    def calculate_frame_delta(self, prev, current):
        if current < 0 or prev < 0:
            raise ValueError("Negative timestamp encountered")
        return (current - prev) / (current + 1e-9)

    @safety_net
    def process_telemetry(self, data):
        if not isinstance(data, dict):
            raise TypeError("Expected telemetry dict")
        return {k: v * 1.5 for k, v in data.items() if v > self.threshold}

if __name__ == "__main__":
    handler = PerformanceHandler()
    print(handler.calculate_frame_delta(100, 105))
    print(handler.process_telemetry({"fps": 60, "ping": 0.002}))