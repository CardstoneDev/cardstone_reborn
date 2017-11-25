from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core_game.state.game_state import GameState


class Event:
    # events never get held so they may be lambdas
    def __init__(self, type: str, variables: {}, perform: 'callable[GameState,dict]'):
        self.type = type
        self.variables = variables
        # TODO
        self.perform = perform


def signal_event(state: 'GameState', variables: dict):
    pass


class SignalEvent(Event):
    def __init__(self, type: str, variables: dict):
        super(SignalEvent, self).__init__(type, variables, signal_event)
