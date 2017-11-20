import unittest

from core_game.state.game_state import GameState
from core_game.state_processor import make_new_game
from core_game.state_serialization import string_to_game_state


def state_equality_check(state1: GameState, state2: GameState, assertion_unit: unittest.TestCase):
    for i in range(len(state1.p0.cards.all_zones)):
        assertion_unit.assertEquals(len(state1.p0.cards.all_zones[i].cards), len(state2.p0.cards.all_zones[i].cards))
        for j in range(len(state1.p0.cards.all_zones[i].cards)):
            assertion_unit.assertTrue(state1.p0.cards.all_zones[i].cards[j].equals(state2.p0.cards.all_zones[
                                                                                       i].cards[j]))

    for i in range(len(state1.p1.cards.all_zones)):
        assertion_unit.assertEquals(len(state1.p1.cards.all_zones[i].cards), len(state2.p1.cards.all_zones[i].cards))
        for j in range(len(state1.p1.cards.all_zones[i].cards)):
            assertion_unit.assertTrue(state1.p1.cards.all_zones[i].cards[j].equals(state2.p1.cards.all_zones[
                                                                                       i].cards[j]))

    assertion_unit.assertEquals(state1.p1.health, state2.p1.health)
    assertion_unit.assertEquals(state1.p0.health, state2.p0.health)
    assertion_unit.assertEquals(state1.p0.mana.full_crystals, state2.p0.mana.full_crystals)
    assertion_unit.assertEquals(state1.p0.mana.empty_crystals, state2.p0.mana.empty_crystals)
    assertion_unit.assertEquals(state1.p1.mana.full_crystals, state2.p1.mana.full_crystals)
    assertion_unit.assertEquals(state1.p1.mana.empty_crystals, state2.p1.mana.empty_crystals)
    assertion_unit.assertTrue(state1.p0.devotion.equals(state2.p0.devotion))
    assertion_unit.assertTrue(state1.p1.devotion.equals(state2.p1.devotion))


def make_demo_game() -> GameState:
    state_str = make_new_game(
        "[\"DrawCreature\",\"DrawCreature\",\"DrawCreature\",\"DrawCreature\",\"DrawCreature\",\"DrawCreature\","
        "\"DrawCreature\"]",
        "[\"DrawCreature\",\"DrawCreature\",\"DrawCreature\",\"DrawCreature\",\"DrawCreature\",\"DrawCreature\","
        "\"DrawCreature\"]",
        "DefaultSettings")

    return string_to_game_state(state_str)
