from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core_game.events.event import Event
    from core_game.state.game_state import GameState
    from core_game.cards import Card
    from core_game.state.card_list import CardList

class EventResponder:
    def __init__(self, res : callable[['Event', 'GameState', dict, 'CardList', 'Card'], list['Event']]):
        self.response = res
        self.stored_state = {}

    def respond_to_event(self, event: 'Event', state: 'GameState', zone : 'CardList', owner : 'Card') -> list['Event']:
        return self.response(event, state, self.stored_state, zone, owner)
