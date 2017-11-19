from core_game.cards.card import Card
from core_game.events.event import Event
from core_game.state.card_list import CardList
from core_game.state.player import Player

def card_zone_change_event(card: Card, start_zone: CardList, end_zone: CardList) -> Event:
    return Event("card_zone_change", {"card": card, "start_zone": start_zone, "end_zone": end_zone})

def mana_spend_event(player: Player, cost: int) -> Event:
    return Event("mana_spend", {"player": player, "cost": cost})
