from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core_game.cards.card import Card
    from core_game.events.event import Event
    from core_game.state.card_list import CardList
    from core_game.state.game_state import GameState


class PlayerCards:
    def __init__(self, deck: 'CardList', hand: 'CardList', graveyard: 'CardList', creatures:
    'CardList', auras: 'CardList'):
        self.deck = deck
        self.hand = hand
        self.graveyard = graveyard
        self.creatures = creatures
        self.auras = auras
        self.all_zones = [deck, hand, graveyard, creatures, auras]

    def preprocess_event(self, event: 'Event', state: 'GameState', already_processed: 'set[Card]') -> ('Card', 'Event'):
        """
        finds the first card that modifies this event, and returns a tuple of card,
        event, containing that card and the new version of the event.
        If no cards want to modify it, returns the original event and none
        """
        for elt in self.all_zones:
            modifier, event = elt.preprocess_event(event, state, already_processed)
            if modifier is not None:
                return (modifier, event)
        return (None, event)

    def respond_to_event(self, event: 'Event', state: 'GameState') -> 'list[Event]':
        lst = []
        for card_list in self.all_zones:
            lst += card_list.respond_to_event(event, state)
        return lst
