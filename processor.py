import random
import json

def process_action(action):
    valid_actions = ['attack', 'defend', 'heal']
    if action not in valid_actions:
        raise ValueError(f"Invalid action: '{action}'. Valid actions are {valid_actions}.")
    return f"Action '{action}' processed successfully."

if __name__ == '__main__':
    actions = ['attack', 'defend', 'heal', 'run']  # Simulating user input
    results = []
    for action in actions:
        try:
            result = process_action(action)
            results.append(result)
        except ValueError as e:
            results.append(str(e))
    print(json.dumps(results, indent=2))
