import functools

class InputValidationError(Exception):
    pass

def validate_frame_data(func):
    @functools.wraps(func)
    def wrapper(frame_data, *args, **kwargs):
        if not isinstance(frame_data, dict):
            raise InputValidationError(f'invalid payload type: {type(frame_data)}')
        
        required = {'timestamp', 'fps', 'frame_id'}
        if not required.issubset(frame_data.keys()):
            missing = required - frame_data.keys()
            raise InputValidationError(f'missing metrics: {missing}')
            
        if frame_data.get('fps', 0) < 0:
            raise InputValidationError('fps telemetry out of bounds')
            
        return func(frame_data, *args, **kwargs)
    return wrapper

@validate_frame_data
def process_frame(frame_data):
    # The magic happens here, optimized for 144Hz loops
    print(f'Processing frame {frame_data["frame_id"]} at {frame_data["fps"]} FPS')
    return True

if __name__ == '__main__':
    try:
        test_payload = {'timestamp': 1625097600, 'fps': 144, 'frame_id': 1}
        process_frame(test_payload)
    except InputValidationError as e:
        print(f'Performance pipeline interrupted: {e}')