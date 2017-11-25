from typing import TYPE_CHECKING

from core_game.events.event_responder import PlayerEventResponder
from core_game.events.event_responder_utils import DefaultPlayerTurnStartResponse

if TYPE_CHECKING:
    from core_game.events.event import Event
    from core_game.state.devotion import Devotion
    from core_game.state.game_state import GameState
    from core_game.state.mana_pool import ManaPool
    from core_game.state.player_cards import PlayerCards
    from core_game.state.card_list import CardList


class Player:
    def __init__(self, cards: 'PlayerCards', devotion: 'Devotion', mana: 'ManaPool', health: int, number: int):
        self.cards = cards
        self.devotion = devotion
        self.mana = mana
        self.health = health
        self.responders = {}
        self.prepare_responders()
        self.number = number

    def prepare_responders(self):
        self.responders['start_turn'] = PlayerEventResponder(DefaultPlayerTurnStartResponse(self))

    def respond_to_event(self, event: 'Event', state: 'GameState') -> 'list[Event]':
        card_ress = self.cards.respond_to_event(event, state)
        devotion_ress = self.devotion.respond_to_event(event, state)
        own_ress = self.internal_response(event, state)
        return card_ress + devotion_ress + own_ress

    def internal_response(self, event: 'Event', state: 'GameState') -> 'list[Event]':
        type = event.type
        if type in self.responders:
            return self.responders[type].respond_to_event(event, state)
        return []
