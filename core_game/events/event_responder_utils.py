from core_game.events.event_responder import EventResponderLambda
from core_game.events.event_utils import card_draw_event, card_zone_change_event, creature_attack_event, \
    creature_damage_event
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
    def __init__(self, res, own_tag="card"):
        """
        :param res:
        :type res:
        :param own_tag: own_tag is the tag this card should have in the variable dictionary.
        It may be a list or a string: string will be interpreted as a single element list
        :type own_tag
        """
        self.res = res
        if type(own_tag) == "str":
            self.own_tags = [own_tag]
        else:
            self.own_tags = own_tag

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
        for elt in self.own_tags:
            if elt in event.variables:
                occurred_to = event.variables["card"]
                if card.equals(occurred_to):
                    return self.res.respond(event, state, zone, card)
        return []


class AttackTarget(EventResponderLambda):
    def respond(self, event, state, zone, card):
        return [creature_attack_event(event.variables["target"], card)]


class BasicCreatureAttackResponse(EventResponderLambda):
    def respond(self, event, state, zone, card):
        do = False
        if card.equals(event.variables["attacker"]):
            do = True
            damager = event.variables["target"]
        elif card.equals(event.variables["target"]):
            do = True
            damager = event.variables["attacker"]
        if do:
            return [creature_damage_event(card, damager.get_attack())]
        return []


class CheckMarkDead(EventResponderLambda):
    def __init__(self, card_to_check):
        self.card_to_check = card_to_check

    def respond(self, event, state, zone, card):
        if card.equals(self.card_to_check):
            if card.is_dead():
                return [card_mark_dead_event(card)]
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


def owner_grave(card: 'Card'):
    return card.get_owner().cards.grave
