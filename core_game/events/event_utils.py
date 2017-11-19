from core_game.cards.card import Card
from core_game.events.event import Event
from core_game.state.card_list import CardList
from core_game.state.game_state import GameState
from core_game.state.player import Player

"""
##################################################################
########################### EVENT CREATORS #######################
##################################################################
"""


def card_zone_change_event(card: Card, start_zone: CardList, end_zone: CardList) -> Event:
    return Event("card_zone_change",
                 {"card": card, "start_zone": start_zone, "end_zone": end_zone}, move_card)


def mana_spend_event(player: Player, cost: int) -> Event:
    return Event("mana_spend", {"player": player, "cost": cost}, spend_mana)

def card_draw_event(player: Player) -> Event:
    return Event("card_draw", {"player": player}, draw_card)

"""
##################################################################
########################### EVENT PERFORMERS #####################
##################################################################
"""


def move_card(state: GameState, variables: dict):
    card = variables['card']
    start_zone = variables['start_zone']
    end_zone = variables['end_zone']
    start_zone.remove(card)
    end_zone.append(card)


def spend_mana(state: GameState, variables: dict):
    player = variables['player']
    cost = variables['cost']
    assert player.mana.full_crystals >= cost
    player.mana.full_crystals -= cost

def draw_card(state: GameState, variables: dict):
    player = variables['player']
    card = player.cards.deck.cards.pop()
    player.cards.hand.cards.append(card)
