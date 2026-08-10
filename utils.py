import json
import random
from datetime import datetime

class GameDataHandler:
    def __init__(self, data):
        self.data = data

    def filter_records(self, key, value):
        return [record for record in self.data if record.get(key) == value]

    def sort_records(self, key, reverse=False):
        return sorted(self.data, key=lambda x: x.get(key), reverse=reverse)

    def get_random_record(self):
        return random.choice(self.data)

    def to_json(self):
        return json.dumps(self.data, default=str)

    @staticmethod
    def from_json(json_str):
        return json.loads(json_str)

    def timestamp_records(self):
        for record in self.data:
            record['timestamp'] = datetime.now().isoformat()

    def average_score(self):
        scores = [record['score'] for record in self.data if 'score' in record]
        return sum(scores) / len(scores) if scores else 0.0
