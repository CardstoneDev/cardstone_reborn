from core_game.devotions.devotion import Devotion
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core_game.events.event import Event

class NoDevotion(Devotion):
    def __init__(self):
        pass

    def respond_to_event(self, event: 'Event') -> 'list[Event]':
        return []
