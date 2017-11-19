from core_game.cards.creature_card import CreatureCard
from core_game.events.event_responder import EventResponder
from core_game.state.player import Player


class DrawCreature(CreatureCard):
    def __init__(self,owner : Player):
        super(owner)
        self.responders['card_played'] = EventResponder(on_self(self,draw_cards(1,owner)))
