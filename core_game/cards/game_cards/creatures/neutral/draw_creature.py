from core_game.cards.creature_card import CreatureCard
from core_game.events.event_responder import EventResponder
from typing import TYPE_CHECKING

from core_game.events.event_responder_utils import OnSelf, DrawCards, Both

if TYPE_CHECKING:
    from core_game.state.player import Player



class DrawCreature(CreatureCard):
    """
    A simple 1/1 for 1 that draws a card on play.
    """
    def __init__(self, owner: 'Player', id : int):
        super(DrawCreature, self).__init__(owner, 1, 1, 1,id)
        self.responders['card_played'] = EventResponder(Both(
            self.responders['card_played'], OnSelf(DrawCards(owner, 1))))

    def get_image(self):
        return None

    def get_name(self):
        return "Cheap Drawsh Creature"

    def get_text(self):
        return "Drawr"
