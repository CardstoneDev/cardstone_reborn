from core_game.cards.card import Card
from core_game.events.event import Event
from core_game.state.game_state import GameState
from typing import Callable, Dict

class EventPreprocessor:
    def __init__(self, res : Callable[[Event, GameState, Dict, str], (bool, Event)]):
        self.preprocessor = res
        self.stored_state = {}

    def preprocess_event(self, event: Event, state: GameState, zone : str, owner : Card) -> (bool, Event):
        return self.preprocessor(event, state, self.stored_state, owner, zone)


