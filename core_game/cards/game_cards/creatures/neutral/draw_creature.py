from core_game.cards.creature_card import CreatureCard
from core_game.events.event_responder import EventResponder
from core_game.state.player import Player
from core_game.events.event_responder_utils import on_self, draw_cards


class DrawCreature(CreatureCard):
    def __init__(self, owner: Player):
        super(DrawCreature, self).__init__(owner, 2, 2, 2)
        self.responders['card_played'] = EventResponder(on_self(self, draw_cards(owner, 1)))