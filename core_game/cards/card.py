import abc

from core_game.events.event import Event
from core_game.events.event_preprocessor import EventPreprocessor
from core_game.events.event_responder import EventResponder
from core_game.state.action import Action
from core_game.state.game_state import GameState
from core_game.state.player import Player
from core_game.state.card_list import CardList


class Card(abc.ABC):
    # TODO: clean up abstractmethods
    def __init__(self, preprocessors: dict[str, EventPreprocessor],
                 responders: dict[str, EventResponder], owner: Player):
        self.preprocessors = preprocessors
        self.responders = responders
        self.owner = owner

    @abc.abstractmethod
    def get_name(self) -> str:
        pass

    @abc.abstractmethod
    def get_image(self) -> str:
        """
        returns the relative path to the image as a string
        """
        pass

    @abc.abstractmethod
    def get_text(self) -> str:
        pass


    def get_cost(self) -> int:
        self.cost

    def get_id(self) -> int:
        pass

    def get_owner(self) -> Player:
        return self.owner

    def allow_action(self, action: Action) -> bool:
        return True

    def preprocess_event(self, event: Event, state: GameState, zone: CardList) -> (bool, Event):
        """
        Accept an event. Return
        """
        type = event.type
        if type in self.preprocessors:
            preprocessed, event = self.preprocessors[type].preprocess_event(event, state, zone, self)
            if preprocessed:
                return preprocessed, event
        return (False, event)

    def respond_to_event(self, event: Event, state: GameState, zone: CardList) -> list[Event]:
        """
        Accept an event. Return a list of new events
        that this card wishes to create and add to the event q.
        This list may be empty.
        """
        type = event.type
        if type in self.responders:
            return self.responder[type].respond(event, state, zone, self)
        return []
