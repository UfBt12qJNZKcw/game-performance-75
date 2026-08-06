import random
import time

def random_delay(min_delay=0.5, max_delay=2.0):
    """Introduce a random delay between operations."""
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)


def handle_player_action(action, player):
    """Handle actions taken by the player."""
    actions = {'jump': player.jump, 'run': player.run, 'shoot': player.shoot}
    if action in actions:
        actions[action]()
        print(f'{player.name} performed {action}')
    else:
        print(f'Unknown action: {action}')


def calculate_score(points, multiplier=1):
    """Calculate the player's score based on points and a multiplier."""
    return points * multiplier


def log_action(action, player_name):
    """Log player actions to the console."""
    print(f'Action logged: {action} by {player_name}')  


def validate_player_input(input_value, valid_inputs):
    """Validate player input against a set of valid options."""
    return input_value in valid_inputs


def display_message(message):
    """Display a message to the player."""
    print(f'Message: {message}')