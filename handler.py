from typing import List, Dict, Any

class GameState:
    """Class to represent the state of the game."""
    def __init__(self, level: int, score: int, player_pos: List[int]) -> None:
        self.level: int = level
        self.score: int = score
        self.player_pos: List[int] = player_pos

    def update_score(self, points: int) -> None:
        """Updates the score of the game."""
        self.score += points

    def move_player(self, new_position: List[int]) -> None:
        """Moves the player to a new position."""
        self.player_pos = new_position

class GameHandler:
    """Class to handle game operations."""
    def __init__(self) -> None:
        self.game_state: GameState = GameState(level=1, score=0, player_pos=[0, 0])

    def handle_event(self, event: Dict[str, Any]) -> None:
        """Handles various game events based on input dictionary."""
        if event['type'] == 'score':
            self.game_state.update_score(event.get('points', 0))
        elif event['type'] == 'move':
            self.game_state.move_player(event['position'])

    def get_game_info(self) -> Dict[str, Any]:
        """Returns the current game information as a dictionary."""
        return {
            'level': self.game_state.level,
            'score': self.game_state.score,
            'player_position': self.game_state.player_pos
        }
