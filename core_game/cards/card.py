import abc

from core_game.events.event import Event
from core_game.events.event_preprocessor import EventPreprocessor
from core_game.events.event_responder import EventResponder
from core_game.state.action import Action
from core_game.state.game_state import GameState


class Card(abc):
    def __init__(self, preprocessors: dict[str, EventPreprocessor],
                 responders: dict[str, EventResponder]):
        self.preprocessors = preprocessors
        self.responders = responders

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

    def get_id(self) -> int:
        pass

    def allow_action(self, action: Action) -> bool:
        return True

    def preprocess_event(self, event: Event, state: GameState) -> (bool, Event):
        """
        Accept an event. Return 
        """
        type = event.type
        if type in self.preprocessors:
            responded, event = self.responders[type].respond_to_event(event, state)
            if responded:
                return responded, event
        return (False, event)

    def respond_to_event(self, event: Event, state: GameState) -> list[Event]:
        """
        Accept an event. Return a list of new events
        that this card wishes to create and add to the event q.
        This list may be empty.
        """
        type = event.type
        if type in self.responders:
            return self.responder[type].respond(event, state)
        return []
