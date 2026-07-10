from typing import List, Dict, Any
import random

class GameCore:
    def __init__(self, max_players: int) -> None:
        """Initializes the game core with a maximum number of players."""
        self.max_players: int = max_players
        self.players: List[str] = []

    def add_player(self, player_name: str) -> bool:
        """Adds a player to the game if not full. Returns success status."""
        if len(self.players) < self.max_players:
            self.players.append(player_name)
            return True
        return False

    def start_game(self) -> List[str]:
        """Randomly shuffles players and starts the game."""
        if len(self.players) < 2:
            raise ValueError("Not enough players to start the game.")
        random.shuffle(self.players)
        return self.players

    def get_player_count(self) -> int:
        """Returns the current number of players."""
        return len(self.players)

    def get_game_state(self) -> Dict[str, Any]:
        """Returns the current game state as a dictionary."""
        return {'players': self.players, 'max_players': self.max_players}
