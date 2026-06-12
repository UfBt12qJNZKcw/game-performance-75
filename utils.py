import json
from datetime import datetime

def format_game_data(raw_data):
    formatted_data = []
    for entry in raw_data:
        formatted_entry = {
            'player_id': entry['id'],
            'score': entry['score'],
            'level': entry.get('level', 1),
            'timestamp': datetime.now().isoformat(),
            'game_mode': entry.get('mode', 'casual'),
            'status': 'active' if entry['score'] > 0 else 'inactive'
        }
        formatted_data.append(formatted_entry)
    return json.dumps(formatted_data, indent=4)

# Example usage:
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'score': 200, 'level': 5},
        {'id': 2, 'score': 0, 'level': 3, 'mode': 'ranked'},
        {'id': 3, 'score': 450}
    ]
    print(format_game_data(sample_data))