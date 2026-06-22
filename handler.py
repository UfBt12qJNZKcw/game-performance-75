import random

class GameError(Exception):
    pass

class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        if amount < 0:
            raise GameError('Damage amount cannot be negative.')
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        if amount < 0:
            raise GameError('Heal amount cannot be negative.')
        self.health += amount
        if self.health > 100:
            self.health = 100

class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        if not isinstance(player, Player):
            raise GameError('Only Player instances can be added.')
        self.players.append(player)

    def attack(self, attacker, target):
        if attacker not in self.players or target not in self.players:
            raise GameError('Both players must be in the game.')
        damage = random.randint(5, 20)
        target.take_damage(damage)

    def get_health_status(self):
        return {player.name: player.health for player in self.players}
