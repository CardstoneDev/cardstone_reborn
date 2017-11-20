from core_game.devotions.devotion import Devotion
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core_game.events.event import Event

class NoDevotion(Devotion):
    def equals(self, other):
        return type(other).__name__ ==  "NoDevotion"

    def __init__(self):
        pass

    def respond_to_event(self, event: 'Event',state) -> 'list[Event]':
        return []


