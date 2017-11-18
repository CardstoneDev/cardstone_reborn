class Player:
    def __init__(self, cards : PlayerCards, devotion : Devotion, mana : ManaPool, health : int):
        self.cards = cards
        self.devotion = devotion
        self.mana = mana
        self.health = health
