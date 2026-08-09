import json
import logging

class GameError(Exception):
    pass

class Game:
    def __init__(self):
        self.state = 'initialized'
        self.players = []

    def add_player(self, player_name):
        if not isinstance(player_name, str) or not player_name:
            logging.error('Invalid player name provided')
            raise GameError('Player name must be a non-empty string')
        self.players.append(player_name)
        logging.info(f'Player {player_name} added successfully')

    def remove_player(self, player_name):
        try:
            self.players.remove(player_name)
            logging.info(f'Player {player_name} removed successfully')
        except ValueError:
            logging.warning(f'Player {player_name} not found')
            raise GameError('Player not found')

    def start_game(self):
        if len(self.players) < 2:
            logging.error('Not enough players to start the game')
            raise GameError('At least 2 players are required')
        self.state = 'started'
        logging.info('Game has started')

    def to_json(self):
        return json.dumps({'state': self.state, 'players': self.players})

