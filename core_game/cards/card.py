import abc
from core_game.events.event_utils import mana_spend_event
from core_game.events.event_responder import BasicEventResponderLambda
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core_game.events.event import Event
    from core_game.events.event_preprocessor import EventPreprocessor
    from core_game.events.event_responder import EventResponder
    from core_game.state.action import Action
    from core_game.state.game_state import GameState
    from core_game.state.player import Player
    from core_game.state.card_list import CardList


def default_on_play(event: 'Event', state: 'GameState', zone: 'CardList',
                    owner: 'Card') -> 'list[Event]':
    # TODO: onself(spend_own_cost)
    """
    The default responder to any card being played
    """
    res = []
    if event.variables['card'].get_id() == owner.get_id():
        res.append(mana_spend_event(owner.get_owner(), owner.get_cost()))
    return res


class Card(abc.ABC):
    # TODO: clean up abstractmethods
    # TODO: builder for cards
    def __init__(self, owner: 'Player', cost: int, id:int):
        self.preprocessors = {}  # type: dict[str, 'EventPreprocessor']
        self.responders = {}  # type: dict[str,'EventResponder']
        self.responders['card_played'] = BasicEventResponderLambda(default_on_play)
        self.owner = owner
        self.cost = cost
        self.id = id

    @abc.abstractmethod
    def get_name(self) -> str:
        pass

    @abc.abstractmethod
    def get_image(self) -> str:
        """
        returns the relative path to the image as a string
        """
        pass

    def equals(self,other):
        return self.get_id() == other.get_id()

    @abc.abstractmethod
    def get_text(self) -> str:
        pass

    def get_cost(self) -> int:
        return self.cost

    def get_id(self) -> int:
        return self.id

    def get_owner(self) -> 'Player':
        return self.owner

    def allow_action(self, action: 'Action') -> bool:
        return True

    def preprocess_event(self, event: 'Event', state: 'GameState', zone: 'CardList') -> (bool, 'Event'):
        """
        Accept an event. Return
        """
        type = event.type
        if type in self.preprocessors:
            preprocessed, event = self.preprocessors[type].preprocess_event(event, state, zone, self)
            if preprocessed:
                return preprocessed, event
        return (False, event)

    def respond_to_event(self, event: 'Event', state: 'GameState', zone: 'CardList') -> 'list[Event]':
        """
        Accept an event. Return a list of new events
        that this card wishes to create and add to the event q.
        This list may be empty.
        """
        type = event.type
        if type in self.responders:
            return self.responders[type].respond_to_event(event, state, zone, self)
        return []
