from core_game.state.devotion import Devotion
from core_game.state.mana_pool import ManaPool
from core_game.state.player_cards import PlayerCards


class Player:
    def __init__(self, cards : PlayerCards, devotion : Devotion, mana : ManaPool, health : int):
        self.cards = cards
        self.devotion = devotion
        self.mana = mana
        self.health = health
