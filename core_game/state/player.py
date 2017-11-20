from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core_game.events.event import Event
    from core_game.state.devotion import Devotion
    from core_game.state.game_state import GameState
    from core_game.state.mana_pool import ManaPool
    from core_game.state.player_cards import PlayerCards

class Player:
    def __init__(self, cards: 'PlayerCards', devotion: 'Devotion', mana: 'ManaPool', health: int):
        self.cards = cards
        self.devotion = devotion
        self.mana = mana
        self.health = health

    def respond_to_event(self, event: 'Event', state: 'GameState') -> 'list[Event]':
        card_ress =  self.cards.respond_to_event(event, state)
        return card_ress + self.devotion.respond_to_event(event, state)
