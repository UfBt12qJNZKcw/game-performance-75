import json
import random

class GameProcessor:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        if not isinstance(player, str) or not player:
            raise ValueError('Player name must be a non-empty string.')
        self.players.append(player)

    def process_action(self, action):
        valid_actions = ['run', 'jump', 'shoot']
        if action not in valid_actions:
            raise ValueError(f'Invalid action: {action}. Valid actions are: {valid_actions}')
        # Randomly simulate success or failure
        success = random.choice([True, False])
        if not success:
            raise RuntimeError('Action processing failed unexpectedly.')
        return f'Action {action} processed successfully.'

    def get_player_stats(self):
        if not self.players:
            raise IndexError('No players available to get stats.')
        return {player: random.randint(1, 100) for player in self.players}

# Example usage
if __name__ == '__main__':
    processor = GameProcessor()
    try:
        processor.add_player('Alice')
        print(processor.process_action('jump'))
        print(processor.get_player_stats())
    except (ValueError, RuntimeError, IndexError) as e:
        print(f'Error: {e}')