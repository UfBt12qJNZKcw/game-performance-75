class GameError(Exception):
    pass

class GameHandler:
    def __init__(self, game_data):
        self.game_data = game_data

    def validate_data(self):
        if not isinstance(self.game_data, dict):
            raise GameError('Game data must be a dictionary.')
        if 'score' not in self.game_data:
            raise GameError('Game data must contain a score.')
        if not isinstance(self.game_data['score'], (int, float)):
            raise GameError('Score must be a number.')
        if self.game_data['score'] < 0:
            raise GameError('Score cannot be negative.')

    def handle_game(self):
        try:
            self.validate_data()
            return self.process_game()
        except GameError as e:
            return {'error': str(e)}

    def process_game(self):
        # Placeholder for game processing logic
        return {'status': 'success', 'score': self.game_data['score']}

# Example usage
handler = GameHandler({'score': 100})
result = handler.handle_game()
print(result)  # Output: {'status': 'success', 'score': 100}  

handler_invalid = GameHandler({'score': -50})
result_invalid = handler_invalid.handle_game()
print(result_invalid)  # Output: {'error': 'Score cannot be negative.'}
