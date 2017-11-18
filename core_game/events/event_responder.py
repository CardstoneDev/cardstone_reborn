from core_game.events.event import Event
from core_game.state.game_state import GameState


class EventResponder:
    def respond_to_event(self, event: Event, state: GameState) -> list[Event]:
        return self.response(event, state, self.stored_state)

    def __init__(self, res):
        self.response = res
        self.stored_state = {}
