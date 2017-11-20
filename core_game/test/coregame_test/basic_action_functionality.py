import unittest

from core_game.state_processor import process
from core_game.state_serialization import string_to_game_state, game_state_to_string
from core_game.test.coregame_test.utils import make_demo_game, state_equality_check


class TestBasicActionFunctionality(unittest.TestCase):
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
        new_state = string_to_game_state(process(action_str,state_str))
        state_equality_check(new_state,state,self)

    def test_basic_end_turn_action(self):
        pass

    def test_basic_spell_targeting_action(self):
        pass

    def test_basic_creature_attack_action(self):
        pass

    def test_basic_player_attack_action(self):
        pass


def do_test():
    tst = TestBasicActionFunctionality()
    tst.test_basic_play_action()