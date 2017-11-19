from devotion import Devotion
from core_game.events.event import Event

class NoDevotion(Devotion):
    def __init__(self):
        pass

    def respond_to_event(self, event: Event) -> list[Event]:
        return []
