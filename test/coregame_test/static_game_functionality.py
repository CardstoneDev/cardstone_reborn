import unittest

from core_game.state.game_state import GameState
from core_game.state_processor import make_new_game
from core_game.state_serialization import string_to_game_state, game_state_to_string
from test.coregame_test.utils import make_demo_game, state_equality_check


class TestStaticGameFunctionality(unittest.TestCase):



    def test_serializing_in_and_out(self):
        state_original = make_demo_game()
        serial_state = game_state_to_string(state_original)
        deserial_state = string_to_game_state(serial_state)
        state_equality_check(state_original,deserial_state,self)


    def test_basic_game_state_creation(self):
        state_original = make_demo_game()
        self.assertEquals(len(state_original.p0.cards.hand.cards), state_original.settings.get_initial_hand_size() + 1)
        self.assertEquals(len(state_original.p1.cards.hand.cards), state_original.settings.get_initial_hand_size())
        self.assertEquals(len(state_original.p0.cards.deck.cards),7 - state_original.settings.get_initial_hand_size() - 1)
        self.assertEquals(len(state_original.p1.cards.deck.cards),
                          7 - state_original.settings.get_initial_hand_size())
        self.assertEquals(state_original.p0.health,state_original.settings.get_initial_health())
        self.assertEquals(state_original.p1.health,state_original.settings.get_initial_health())
        self.assertEquals(state_original.p0.mana.full_crystals,state_original.settings.get_initial_mana())
        self.assertEquals(state_original.p1.mana.full_crystals,0)
        self.assertEquals(type(state_original.p0.devotion).__name__,"NoDevotion")
        self.assertEquals(type(state_original.p1.devotion).__name__,"NoDevotion")
        self.assertEquals(len(state_original.p0.cards.creatures.cards),0)
        self.assertEquals(len(state_original.p0.cards.graveyard.cards),0)
        self.assertEquals(len(state_original.p0.cards.auras.cards),0)
        self.assertEquals(len(state_original.p1.cards.creatures.cards),0)
        self.assertEquals(len(state_original.p1.cards.graveyard.cards),0)
        self.assertEquals(len(state_original.p1.cards.auras.cards),0)

if __name__ == '__main__':
    unittest.main()