class PlayerCards:
    def __init__(self,deck : CardList, hand : CardList, graveyard : CardList, creatures :
                 CardList, auras : CardList):
        self.deck = deck
        self.hand = hand
        self.graveyard = graveyard
        self.creatures = creatures
        self.auras = auras