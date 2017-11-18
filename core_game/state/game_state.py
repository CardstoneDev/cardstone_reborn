from collections import deque

from core_game.state.action import Action
from core_game.state.player import Player


class GameState:
    def __init__(self, p0: Player, p1: Player, turn: int):
        self.p0 = p0
        self.p1 = p1
        self.turn = turn

    def can_do(self, action: Action) -> bool:
        """
        Takes in an action and returns true if that action can be
        performed on this state, false otherwise.
        """
        pass

    def do(self, action: Action) -> str:
        """
        Takes in an action and attempts to perform that action on this state.
        If the action was performed successfully, returns None
        If the action cannot be performed, returns "error: " followed by a descriptive error message.
        If the action caused the game to end, returns "end: " follwed by either 0 or 1, where 0
        indicates player 0 won and 1 indicates player 1 won.
        If the action requires further input from one or both of the players, the resulting GameState will reflect this.
        """
        try:
            events_to_do = deque()
            events_to_do.append(action.get_event(self))
            while len(events_to_do) != 0:
                event = events_to_do.popleft()
                event = self.preproces_event(event)
                new_events = self.handle_event(event)
                for elt in new_events:
                    events_to_do.append(elt)
        except:
            return "error: fuck"
