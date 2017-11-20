from core_game.events.event_responder import EventResponderLambda
from core_game.events.event_utils import card_draw_event, card_zone_change_event
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

    def respond(self, event, state, zone, card):
        """
        :param event:
        :type event: core_game.events.event.Event
        :param state:
        :type state: core_game.state.game_state.GameState
        :param zone:
        :type zone: core_game.state.card_list.CardList
        :param card:
        :type card: core_game.cards.game_cards.creatures.neutral.draw_creature.DrawCreature
        :return:
        :rtype: List
        """
        res = []
        res += self.sub1.respond(event, state, zone, card)
        res += self.sub2.respond(event, state, zone, card)
        return res


class OnSelf(EventResponderLambda):
    def __init__(self, res):
        """
        :param res:
        :type res: EventResponderLambda
        """
        self.res = res

    def respond(self, event, state, zone, card):
        """
        :param event:
        :type event: core_game.events.event.Event
        :param state:
        :type state: core_game.state.game_state.GameState
        :param zone:
        :type zone: core_game.state.card_list.CardList
        :param card:
        :type card: core_game.cards.card.Card
        :return:
        :rtype: List
        """
        if "card" in event.variables:
            occurred_to = event.variables["card"]
            if card.equals(occurred_to):
                return self.res.respond(event, state, zone, card)
        return []


class MoveSelf(EventResponderLambda):
    def __init__(self, target_make):
        """
        :param target_make:
        :type target_make: function
        """
        self.target_make = target_make

    def respond(self, event, state, zone, card):
        """
        :param event:
        :type event: core_game.events.event.Event
        :param state:
        :type state: core_game.state.game_state.GameState
        :param zone:
        :type zone: core_game.state.card_list.CardList
        :param card:
        :type card: core_game.cards.game_cards.creatures.neutral.draw_creature.DrawCreature
        :return:
        :rtype: List[core_game.events.event.Event]
        """
        return [card_zone_change_event(card, zone, self.target_make(card))]


class DrawCards(EventResponderLambda):
    def __init__(self, player, number):
        """
        :param player:
        :type player: core_game.state.player.Player
        :param number:
        :type number: int
        """
        self.player = player
        self.number = number

    def respond(self, event, state, zone, card):
        """
        :type zone: core_game.state.card_list.CardList
        :type card: core_game.cards.card.Card
        :type state: core_game.state.game_state.GameState
        :type event: core_game.events.event.Event
        """
        return [card_draw_event(self.player)] * self.number


def owner_creatures(card):
    """
    :param card:
    :type card: core_game.cards.game_cards.creatures.neutral.draw_creature.DrawCreature
    :return:
    :rtype: core_game.state.card_list.CardList
    """
    return card.get_owner().cards.creatures
