import functools
import logging

class PerformanceConstraintError(Exception):
    pass

def validate_frame_budget(threshold_ms=16.67):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import time
            start = time.perf_counter()
            try:
                result = func(*args, **kwargs)
                duration = (time.perf_counter() - start) * 1000
                if duration > threshold_ms:
                    logging.warning(f'Frame budget exceeded: {duration:.2f}ms')
                return result
            except Exception as e:
                logging.error(f'Critical render pipeline failure: {e}')
                return None
        return wrapper
    return decorator

def robust_input_sanitizer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not args and not kwargs:
            return None
        try:
            return func(*args, **kwargs)
        except (ValueError, TypeError, KeyError) as e:
            logging.critical(f'Sanitization override triggered: {type(e).__name__}')
            return {'status': 'safe_default', 'payload': None}
    return wrapper