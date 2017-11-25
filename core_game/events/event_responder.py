import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core_game.events.event import Event
    from core_game.state.game_state import GameState
    from core_game.cards import Card
    from core_game.state.card_list import CardList


class EventResponder:
    def __init__(self, res):
        self.response = res

    def respond_to_event(self, event: 'Event', state: 'GameState', zone: 'CardList', card: 'Card'):
        return self.response.respond(event, state, zone, card)


class EventResponderLambda(abc.ABC):
    @abc.abstractmethod
    def respond(self, event, state, zone, card):
        pass


class BasicEventResponderLambda(EventResponderLambda):
    def __init__(self, res):
        self.res = res

    def respond(self, event, state, zone, card):
        return self.res(event, state, zone, card)
