from core_game.cards.card import Card
from core_game.events.event import Event
from core_game.state.game_state import GameState

class CardList:
    def __init__(self, cards: list[Card], zone: str):
        self.cards = cards
        self.zone = zone

    # TODO convenience functions as needed
    def preprocess_event(self, event: Event, state: GameState, already_processed: set[Card]) -> (Card, Event):
        """
        finds the first card that modifies this event, and returns a tuple of card,
        event, containing that card and the new version of the event.
        If no cards want to modify it, returns the original event and none of
        """
        for card in self.cards:
            if card not in already_processed:
                changed, event = card.preprocess_event(event, state, self.zone)
                if changed:
                    return (card, event)

        return (None, event)

    def respond_to_event(self, event: Event, state: GameState) -> list[Event]:
        lst = []
        for card in self.cards:
            lst += card.respond_to_event(event, state, self.zone)
        return lst
