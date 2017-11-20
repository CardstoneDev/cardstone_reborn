from core_game.events.event_responder import EventResponderLambda
from core_game.events.event_utils import card_draw_event
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core_game.cards.card import Card
    from core_game.events.event import Event
    from core_game.state.game_state import GameState
    from core_game.state.card_list import CardList
    from core_game.state.player import Player

"""
###########

"""


class Both(EventResponderLambda):
    def __init__(self, sub1, sub2):
        self.sub1 = sub1
        self.sub2 = sub2

    def respond(self, event, state, zone, owner):
        res = []
        res += self.sub1.respond(event, state, zone, owner)
        res += self.sub2.respond(event, state, zone, owner)
        return res


class OnSelf(EventResponderLambda):
    def __init__(self,card,res):
        self.card = card
        self.res = res

    def respond(self,event,state,zone,card):
        if "card" in event.variables:
            occurred_to = event.variables["card"]
            if self.card.equals(occurred_to):
                return self.res.respond(event,state,zone,card)
        return []


class DrawCards(EventResponderLambda):
    def __init__(self,player,number):
        self.player = player
        self.number = number

    def respond(self,event,state,zone,card):
        return [card_draw_event(self.player)] * self.number
