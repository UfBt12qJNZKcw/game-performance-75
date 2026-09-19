import sys

def sanitize_input(user_input):
    try:
        action, val = user_input.split(':', 1)
        return action.strip().lower(), float(val)
    except (ValueError, AttributeError):
        return None, None

def game_loop():
    print('--- Game Engine Initialized ---')
    valid_commands = {'move', 'jump', 'fire'}
    
    while True:
        try:
            raw = input('input (cmd:val)> ')
            if raw == 'exit':
                break
            
            cmd, val = sanitize_input(raw)
            
            if cmd not in valid_commands:
                print(f'rejected invalid command: {cmd}')
                continue
            
            if not (0 <= val <= 100):
                print(f'clamping out-of-bounds value: {val}')
                val = max(0, min(100, val))
                
            print(f'processed {cmd} with intensity {val}')
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f'critical loop error: {e}')

if __name__ == '__main__':
    game_loop()