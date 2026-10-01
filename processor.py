import sys

def validate_frame_data(data):
    expected = {'player_id': int, 'x': float, 'y': float, 'action': str}
    for key, expected_type in expected.items():
        if not isinstance(data.get(key), expected_type):
            raise ValueError(f'malformed packet payload: {key}')
    return True

def process_game_loop(input_queue):
    while True:
        try:
            frame = input_queue.get(timeout=1)
            if validate_frame_data(frame):
                execute_frame_logic(frame)
        except (ValueError, KeyError) as e:
            print(f'input corruption detected: {e}')
            continue
        except Exception:
            break

def execute_frame_logic(frame):
    # simulated game engine frame update
    delta = frame['x'] + frame['y']
    return delta

if __name__ == '__main__':
    # usage example for main process loop
    print('performance-75 engine initialized')
