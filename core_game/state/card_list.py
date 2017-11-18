from core_game.cards.card import Card
from core_game.events.event import Event
from core_game.state.game_state import GameState


class CardList:
    def __init__(self,cards : list[Card]):
        self.cards = cards

    # TODO convenience functions as needed
    def preprocess_event(self, event: Event, state: GameState, already_processed: set[Card]) -> (Card, Event):
        """
        finds the first card that modifies this event, and returns a tuple of card,
        event, containing that card and the new version of the event.
        If no cards want to modify it, returns the original event and none
        """
        for elt in self.cards:
            if elt not in already_processed:
                changed, event = elt.preprocess_event(event, state)
                if changed:
                    return (elt, event)

        return (None, event)
