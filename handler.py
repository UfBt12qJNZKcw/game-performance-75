import random
import logging

logger = logging.getLogger(__name__)

class GameHandler:
    def __init__(self):
        self.players = []
        self.scoreboard = {}

    def add_player(self, player_name):
        if player_name not in self.players:
            self.players.append(player_name)
            self.scoreboard[player_name] = 0
            logger.info(f'Added player: {player_name}')
        else:
            logger.warning(f'Player {player_name} already exists.')

    def remove_player(self, player_name):
        if player_name in self.players:
            self.players.remove(player_name)
            del self.scoreboard[player_name]
            logger.info(f'Removed player: {player_name}')
        else:
            logger.warning(f'Player {player_name} not found.')

    def update_score(self, player_name, points):
        if player_name in self.scoreboard:
            self.scoreboard[player_name] += points
            logger.info(f'Updated score for {player_name}: {self.scoreboard[player_name]}')
        else:
            logger.warning(f'Player {player_name} not in scoreboard.')

    def get_winner(self):
        if not self.scoreboard:
            logger.warning('No players in the game.')
            return None
        winner = max(self.scoreboard, key=self.scoreboard.get)
        logger.info(f'Winner is: {winner}')
        return winner

    def reset_game(self):
        self.players.clear()
        self.scoreboard.clear()
        logger.info('Game has been reset.')