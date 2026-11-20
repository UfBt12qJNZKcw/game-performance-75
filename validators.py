import functools
import logging

class PerformanceValidationError(Exception):
    pass

def robust_input_guard(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if result is None:
                raise PerformanceValidationError("Null metric detected in frame processing")
            return result
        except (TypeError, ValueError, ZeroDivisionError) as e:
            logging.error(f"Invalid telemetry data stream: {e}")
            return None
    return wrapper

class MetricValidator:
    @staticmethod
    @robust_input_guard
    def validate_fps(fps_value):
        """Sanitizes framerate data, caps at 1000 and filters anomalies"""
        fps = float(fps_value)
        if fps < 0:
            raise PerformanceValidationError("Negative fps detected")
        return min(fps, 1000.0)

    @staticmethod
    def frame_sanity_check(data_packet):
        """Ensures frame packet contains essential timing nodes"""
        required = ['delta', 'draw_calls', 'gpu_temp']
        if not all(k in data_packet for k in required):
            missing = [k for k in required if k not in data_packet]
            raise PerformanceValidationError(f"Missing keys: {missing}")
        return True