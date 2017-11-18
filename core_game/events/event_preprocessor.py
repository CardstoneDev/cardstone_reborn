from core_game.cards.card import Card
from core_game.events.event import Event
from core_game.state.game_state import GameState


class EventPreprocessor:
    def preprocess_event(self, event: Event, state: GameState) -> (bool, Event):
        return self.preprocessor(event, state, self.stored_state, self.owner)

    def __init__(self, res, owner: Card):
        self.owner = owner
        self.preprocessor = res
        self.stored_state = {}
