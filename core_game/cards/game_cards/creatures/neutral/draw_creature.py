from core_game.cards.creature_card import CreatureCard
from core_game.events.event_responder import EventResponder
from core_game.events.event_responder_utils import on_self, draw_cards
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core_game.state.player import Player



class DrawCreature(CreatureCard):
    def __init__(self, owner: 'Player'):
        super(DrawCreature, self).__init__(owner, 2, 2, 2)
        self.responders['card_played'] = EventResponder(on_self(self, draw_cards(owner, 1)))

    def get_image(self):
        return None

    def get_name(self):
        return "Cheap Drawsh Creature"

    def get_text(self):
        return "Drawr"
