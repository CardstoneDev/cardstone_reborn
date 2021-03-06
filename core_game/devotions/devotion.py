import abc

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core_game.events.event import Event
    from core_game.state.action import Action


class Devotion(abc.ABC):
    def allow_action(self, action: 'Action') -> bool:
        return True

    @abc.abstractmethod
    def respond_to_event(self, event: 'Event', state) -> 'list[Event]':
        """
        Accept an event. Return a list of new events
        that this card wishes to create and add to the event q.
        This list may be empty.
        """
        pass

    @abc.abstractmethod
    def equals(self,other):
        pass