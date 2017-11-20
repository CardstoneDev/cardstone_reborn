import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core_game.cards.card import Card
    from core_game.events.event import Event
    from core_game.state.game_state import GameState
    from core_game.state.card_list import CardList


class EventPreprocessor:
    def __init__(self, res: PreprocessorLambda):
        self.preprocessor = res

    def preprocess_event(self, event: 'Event', state: 'GameState', zone: 'CardList', owner: 'Card') -> (bool, 'Event'):
        return self.preprocessor.respond(event, state, zone, owner)


class PreprocessorLambda(abc.ABC):
    @abc.abstractmethod
    def respond(self, event, state, zone, owner):
        pass


class BasicPreprocessorLambda(PreprocessorLambda):
    def __init__(self, res):
        self.res = res

    def respond(self, event, state, zone, owner):
        self.res(event, state, zone, owner)
