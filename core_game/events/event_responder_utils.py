from core_game.cards.card import Card
from core_game.events.event import Event
from core_game.state.game_state import GameState
from core_game.state.card_list import CardList
from core_game.events.event_utils import card_draw_event
from core_game.state.player import Player

"""
###########

"""


def r_and(sub1: callable[[Event, GameState, dict, CardList, Card], list[Event]],
          sub2: callable[[Event, GameState, dict, CardList, Card], list[Event]]
          ) -> callable[[Event, GameState, dict, CardList, Card], list[Event]]:
    def result(event: Event, state: GameState, variables: dict, zone: CardList, card: Card) -> list[Event]:
        res_list = []
        res_list += sub1(event, state, variables, zone, card)
        res_list += sub2(event, state, variables, zone, card)
        return res_list

    return result


def on_self(self_card: Card, res: callable[[Event, GameState, dict, CardList, Card], list[Event]]
            ) -> callable[[Event, GameState, dict, CardList, Card], list[Event]]:
    def result(event: Event, state: GameState, variables: dict, zone: CardList, card: Card) -> list[Event]:
        if self_card.get_id() == card.get_id():
            return res(event, state, variables, zone, card)
        return []

    return result


def draw_cards(player: Player, number: int) -> callable[[Event, GameState, dict, CardList, Card], list[Event]]:
    def result(event: Event, state: GameState, variables: dict, zone: CardList, card: Card) -> list[Event]:
        return [card_draw_event(player)] * number

    return result
