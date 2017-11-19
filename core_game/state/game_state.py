from collections import deque

from core_game.cards.card import Card
from core_game.events.event import Event
from core_game.state.action import Action
from core_game.state.player import Player
from core_game.state.settings import SETTINGS


class GameState:
    def __init__(self, p0: Player, p1: Player, turn: int, settings:SETTINGS):
        self.p0 = p0
        self.p1 = p1
        self.turn = turn
        self.settings = SETTINGS

    def can_do(self, action: Action) -> bool:
        """
        Takes in an action and returns true if that action can be
        performed on this state, false otherwise.
        """
        pass
 
    def preprocess_event(self, event: Event) -> Event:
        already_processed = set()  # type: set[Card]
        done = False
        while not done:
            modifier, event = self.p1.cards.preprocess_event(event, self, already_processed)
            if modifier is not None:
                already_processed.add(modifier)
                continue
            modifier, event = self.p0.cards.preprocess_event(event, self, already_processed)
            if modifier is not None:
                already_processed.add(modifier)
                continue
            else:
                done = True
        return event

    def handle_event(self, event: Event) -> list[Event]:
        lst = self.p1.respond_to_event(event, self)
        lst += self.p0.respond_to_event(event, self)
        return lst

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
            events_to_do = deque()  # type: deque[Event]
            events_to_do.append(action.get_event(self))
            while len(events_to_do) != 0:
                event = events_to_do.popleft()
                event = self.preprocess_event(event)
                new_events = self.handle_event(event)
                for elt in new_events:
                    events_to_do.append(elt)
        except:
            return "error: fuck"
