from core_game.cards.card import Card
from core_game.events.event import Event
from core_game.events.event_responder import EventResponder
from core_game.state.game_state import GameState
from core_game.state.card_list import CardList
from core_game.events.event_utils import card_zone_change_event, mana_spend_event
from core_game.state.player import Player


def default_on_play(event: Event, state: GameState, stored_state: dict, zone: CardList, owner: Card) -> list[Event]:
    """
    The default responder to any card being played
    """
    res = []
    if event.variables['card'].get_id() == owner.get_id():
        res += card_zone_change_event(owner, zone, owner.get_owner().cards.creatures)
        res += mana_spend_event(owner.get_owner(), owner.get_cost())
    return res


class CreatureCard(Card):
    def __init__(self,owner : Player):
        super(owner)
        self.responders["card_played"] = EventResponder(default_on_play)

