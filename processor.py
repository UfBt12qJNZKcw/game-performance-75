import json
from collections import defaultdict

def process_game_data(game_data):
    stats = defaultdict(lambda: {'plays': 0, 'wins': 0, 'losses': 0})
    for entry in game_data:
        player_id = entry['player_id']
        result = entry['result']
        stats[player_id]['plays'] += 1
        if result == 'win':
            stats[player_id]['wins'] += 1
        elif result == 'loss':
            stats[player_id]['losses'] += 1
    return json.dumps(stats, indent=4)

if __name__ == '__main__':
    sample_data = [
        {'player_id': '123', 'result': 'win'},
        {'player_id': '123', 'result': 'loss'},
        {'player_id': '456', 'result': 'win'},
        {'player_id': '123', 'result': 'win'},
        {'player_id': '456', 'result': 'loss'}
    ]
    result = process_game_data(sample_data)
    print(result)
