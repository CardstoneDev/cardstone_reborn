from core_game.cards.card import Card
from core_game.events.event_responder_utils import Both, OnSelf, MoveSelf, owner_creatures
from core_game.events.event_utils import card_zone_change_event
from core_game.events.event_responder import BasicEventResponderLambda
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core_game.events.event import Event
    from core_game.events.event_responder import EventResponder
    from core_game.state.game_state import GameState
    from core_game.state.card_list import CardList
    from core_game.state.player import Player


class CreatureCard(Card):
    def __init__(self, owner: 'Player', health: int, attack: int, cost: int, id: int):
        super(CreatureCard, self).__init__(owner, cost, id)
        self.responders["card_played"] = Both(self.responders["card_played"], OnSelf(MoveSelf(owner_creatures)))
        self.health = health
        self.attack = attack

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack
