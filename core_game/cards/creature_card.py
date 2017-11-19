from core_game.cards.card import Card
from core_game.events.event import Event
from core_game.state.game_state import GameState


def default_summon(event: Event, state: GameState, stored_state, owner: Card):
    res = []
    if event.variables['card_id'] == owner.get_id():
        card_id(ID), zone_start(card_list), zone_end(card_list)
        res.append(Event('card_zone_change', {'card_id': owner.get_id(), 'zone_start':}))
    return res


class CreatureCard(Card):
    def __init__(self):
        super()
        self.responders["card_played"] = default_summon
