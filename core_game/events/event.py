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
