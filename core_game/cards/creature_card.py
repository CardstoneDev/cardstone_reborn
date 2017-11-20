from core_game.cards.card import Card
from core_game.events.event_responder_utils import Both
from core_game.events.event_utils import card_zone_change_event
from core_game.events.event_responder import BasicEventResponderLambda
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core_game.events.event import Event
    from core_game.events.event_responder import EventResponder
    from core_game.state.game_state import GameState
    from core_game.state.card_list import CardList
    from core_game.state.player import Player


def default_on_play(event: 'Event', state: 'GameState', zone: 'CardList', owner: 'Card') -> "list['Event']":
    #TODO: onself(moveself)
    """
    The default responder to any card being played
    """
    res = []
    if event.variables['card'].get_id() == owner.get_id():
        res.append(card_zone_change_event(owner, zone, owner.get_owner().cards.creatures))
    return res


class CreatureCard(Card):
    def __init__(self,owner : 'Player',health : int, attack: int, cost: int, id : int):
        super(CreatureCard, self).__init__(owner, cost,id)
        self.responders["card_played"] = Both(self.responders["card_played"],
                                              BasicEventResponderLambda(default_on_play))
        self.health = health
        self.attack = attack

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack
