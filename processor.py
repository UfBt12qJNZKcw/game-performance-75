from typing import List, Dict

class GameProcessor:
    """Class to handle game data processing."""

    def __init__(self, game_data: List[Dict[str, str]]) -> None:
        """Initialize the GameProcessor with game data.

        Args:
            game_data (List[Dict[str, str]]): List of games with attributes.
        """
        self.game_data = game_data

    def filter_games(self, criterion: str) -> List[Dict[str, str]]:
        """Filter games based on a given criterion.

        Args:
            criterion (str): The attribute to filter games by.

        Returns:
            List[Dict[str, str]]: Filtered list of games.
        """
        return [game for game in self.game_data if game['genre'] == criterion]

    def sort_games(self, key: str) -> List[Dict[str, str]]:
        """Sort games based on a specified key.

        Args:
            key (str): The attribute to sort games by.

        Returns:
            List[Dict[str, str]]: Sorted list of games.
        """
        return sorted(self.game_data, key=lambda game: game[key])

    def game_summary(self) -> str:
        """Generate a summary of all games.

        Returns:
            str: Summary string of all games.
        """
        return '\n'.join([f"{game['title']} - {game['genre']}" for game in self.game_data])

# Example usage
if __name__ == '__main__':
    sample_data = [
        {'title': 'Game A', 'genre': 'RPG'},
        {'title': 'Game B', 'genre': 'FPS'},
        {'title': 'Game C', 'genre': 'RPG'},
    ]
    processor = GameProcessor(sample_data)
    print(processor.game_summary())
    print(processor.filter_games('RPG'))
    print(processor.sort_games('title'))
