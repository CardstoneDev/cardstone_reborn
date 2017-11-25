import unittest

from core_game.state_processor import process
from core_game.state_serialization import string_to_game_state, game_state_to_string
from core_game.test.coregame_test.utils import make_demo_game, state_equality_check


class TestBasicActionFunctionality(unittest.TestCase):
    def find_and_play_basic_creature_for_p0(self, state):
        creature = None
        ind = 0
        for elt in state.p0.cards.hand.cards:
            if type(elt).__name__ == "DrawCreature":
                creature = elt
                break
            ind += 1

        state.p0.cards.creatures.cards.append(creature)
        state.p0.cards.hand.cards.pop(ind)
        state.p0.mana.full_crystals -= 1
        drawn = state.p0.cards.deck.cards.pop()
        state.p0.cards.hand.cards.append(drawn)
        return creature

    def test_basic_play_action(self):
        state = make_demo_game()
        state_str = game_state_to_string(state)
        creature = None
        ind = 0
        for elt in state.p0.cards.hand.cards:
            if type(elt).__name__ == "DrawCreature":
                creature = elt
                break
            ind += 1

        state.p0.cards.creatures.cards.append(creature)
        state.p0.cards.hand.cards.pop(ind)
        state.p0.mana.full_crystals -= 1
        drawn = state.p0.cards.deck.cards.pop()
        state.p0.cards.hand.cards.append(drawn)
        action_str = '{"type": "card_played", "player":0, "details":{"card_id":' + str(creature.get_id()) + '}}'
        new_state = string_to_game_state(process(action_str, state_str))
        state_equality_check(new_state, state, self)

    def test_basic_end_turn_action(self):
        state = make_demo_game()
        state_str = game_state_to_string(state)
        state.p0.mana.empty_crystals += 3
        state.p1.mana.empty_crystals += 3
        state.p0.mana.full_crystals += 3
        state.p1.mana.full_crystals += 3

        for x in range(3):
            drawn_0 = state.p0.cards.deck.cards.pop()
            drawn_1 = state.p1.cards.deck.cards.pop()
            state.p0.cards.hand.cards.append(drawn_0)
            state.p1.cards.hand.cards.append(drawn_1)

        p = 0
        for x in range(6):
            action_str = '{"type": "end_turn", "player":' + str(p) + ', "details":{}}'
            state_str = process(action_str, state_str)
            if p == 0:
                p = 1
            else:
                p = 0

        new_state = string_to_game_state(state_str)
        state_equality_check(state, new_state, self)

    def test_basic_spell_targeting_action(self):
        pass

    def test_basic_creature_attack_action(self):
        pass

    def test_basic_player_attack_action(self):
        pass


def do_test():
    tst = TestBasicActionFunctionality()
    tst.test_basic_play_action()
    tst.test_basic_end_turn_action()
