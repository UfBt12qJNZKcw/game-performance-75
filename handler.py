import json
from typing import Any, Dict, List

class GameDataHandler:
    def __init__(self, data: List[Dict[str, Any]]) -> None:
        self.data = data

    def filter_data(self, key: str, value: Any) -> List[Dict[str, Any]]:
        return [entry for entry in self.data if entry.get(key) == value]

    def aggregate_scores(self) -> Dict[str, int]:
        aggregated = {}
        for entry in self.data:
            player = entry['player']
            score = entry['score']
            aggregated[player] = aggregated.get(player, 0) + score
        return aggregated

    def export_to_json(self, filename: str) -> None:
        with open(filename, 'w') as json_file:
            json.dump(self.data, json_file, indent=4)

# Example Usage:
# data = [{'player': 'Alice', 'score': 10}, {'player': 'Bob', 'score': 5}, {'player': 'Alice', 'score': 15}]
# handler = GameDataHandler(data)
# handler.export_to_json('game_data.json')