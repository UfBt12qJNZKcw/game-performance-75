import functools

class InputValidationError(Exception):
    pass

def validate_frame_data(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        data = args[0] if args else kwargs.get('data')
        if not isinstance(data, dict):
            raise InputValidationError('input must be a dict')
        if 'fps' not in data or not (0 < data['fps'] < 1000):
            raise InputValidationError('invalid frame rate threshold')
        return func(*args, **kwargs)
    return wrapper

@validate_frame_data
def process_frame(data):
    return f"processing {data['fps']} fps with latency {data.get('ms', 0)}ms"

def loop_controller(stream):
    for raw_packet in stream:
        try:
            payload = eval(raw_packet)
            print(process_frame(payload))
        except (SyntaxError, InputValidationError, KeyError) as e:
            print(f"frame drop due to: {e}")
            continue