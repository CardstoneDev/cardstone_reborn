from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core_game.state.game_state import GameState



class Event:
    def __init__(self, type: str, variables: {},perform : 'callable[GameState,dict]'):
        self.type = type
        self.variables = variables
        self.perform = perform
