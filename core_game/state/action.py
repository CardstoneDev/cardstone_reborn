import abc

from core_game.events.event import Event
from core_game.state.game_state import GameState


class Action(abc):
    @abc.abstractmethod
    def get_event(self, state: GameState) -> Event:
        pass
