from core_game.events.event import Event
from core_game.state.game_state import GameState
from typing import Callable, Dict, List

class EventResponder:
    def __init__(self, res : Callable[[Event, GameState, Dict, str, Card], list[Event]]):
        self.response = res
        self.stored_state = {}

    def respond_to_event(self, event: Event, state: GameState, zone : str, owner : Card) -> list[Event]:
        return self.response(event, state, self.stored_state, zone, owner)
