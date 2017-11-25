from core_game.events.event import Event, SignalEvent
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core_game.cards.card import Card
    from core_game.state.card_list import CardList
    from core_game.state.game_state import GameState
    from core_game.state.player import Player

"""
##################################################################
########################### EVENT CREATORS #######################
##################################################################
"""


def card_zone_change_event(card: 'Card', start_zone: 'CardList', end_zone: 'CardList') -> 'Event':
    return Event("card_zone_change",
                 {"card": card, "start_zone": start_zone, "end_zone": end_zone}, move_card)


def mana_spend_event(player: 'Player', cost: int) -> 'Event':
    return Event("mana_spend", {"player": player, "cost": cost}, spend_mana)


def card_draw_event(player: 'Player') -> 'Event':
    return Event("card_draw", {"player": player}, draw_card)


def creature_attack_event(attacker: 'Card', target: 'Card'):
    return SignalEvent("creature_attack", {'attacker': attacker, "target": target})


def creature_damage_event(creature: 'Card', damage: int):
    return Event("creature_damage", {"creatue": creature, "damage": damage}, damage_creature)


def creature_death_event(creature: 'Card'):
    return SignalEvent("creature_death", {"creature": creature})


def turn_end_event():
    return Event("end_turn", {}, end_turn)


def turn_start_event():
    return SignalEvent("start_turn", {})


def mana_gain_empty_event(player: 'Player', amount: int, is_turn_start=False):
    return Event("mana_gain_empty", {'player': player, 'amount': amount, "is_turn_state": is_turn_start},
                 gain_empty_mana)


def mana_refresh_event(player: 'Player', is_turn_start=False):
    return Event("mana_refresh", {'player': player, 'is_turn_start': is_turn_start}, refresh_mana)


"""
##################################################################
########################### EVENT PERFORMERS #####################
##################################################################
"""


def refresh_mana(state: 'GameState', variables: dict):
    player = variables['player']
    player.mana.full_crystals = player.mana.empty_crystals


def gain_empty_mana(state: 'GameState', variables: dict):
    amount = variables["amount"]
    player = variables["player"]
    player.mana.empty_crystals += amount


def end_turn(state: 'GameState', variables: dict):
    turn = state.turn
    if turn == 1:
        state.turn = 0
    else:
        state.turn = 1
    return [turn_start_event()]


def damage_creature(state: 'GameState', variables: dict):
    creature = variables['creature']
    damage = variables['damage']
    creature.take_damage(damage)


def move_card(state: 'GameState', variables: dict):
    card = variables['card']
    start_zone = variables['start_zone']
    end_zone = variables['end_zone']
    start_zone.cards.remove(card)
    end_zone.cards.append(card)


def spend_mana(state: 'GameState', variables: dict):
    player = variables['player']
    cost = variables['cost']
    assert player.mana.full_crystals >= cost
    player.mana.full_crystals -= cost


def draw_card(state: 'GameState', variables: dict):
    player = variables['player']
    card = player.cards.deck.cards.pop()
    player.cards.hand.cards.append(card)
