import unittest

from core_game.state.game_state import GameState
from core_game.state_processor import make_new_game
from core_game.state_serialization import string_to_game_state, game_state_to_string


class TestStringMethods(unittest.TestCase):

    def test_serializing_in_and_out(self):
        state_str = make_new_game("draw_1_creature,draw_1_creature,draw_1_creature,draw_1_creature,deal_2_spell,deal_2_spell,deal_2_spell",
                          "draw_1_creature,draw_1_creature,draw_1_creature,draw_1_creature,deal_2_spell,deal_2_spell,deal_2_spell","DefaultSettings")

        state_original = string_to_game_state(state_str) #type: GameState
        serial_state = game_state_to_string(state_original)
        deserial_state = string_to_game_state(serial_state)
        for i in range(len(state_original.p0.cards.all_zones)):
            for j in range(len(state_original.p0.cards.all_zones[i].cards)):
                self.assertEquals(state_original.p0.cards.all_zones[i].cards[j].get_id(),
                                  deserial_state.p0.cards.all_zones[i].cards[j].get_id())

        for i in range(len(state_original.p1.cards.all_zones)):
            for j in range(len(state_original.p1.cards.all_zones[i].cards)):
                self.assertEquals(state_original.p1.cards.all_zones[i].cards[j].get_id(),
                                  deserial_state.p1.cards.all_zones[i].cards[j].get_id())

    def test_basic_game_state_creation(self):
        state_str = make_new_game(
            "draw_1_creature,draw_1_creature,draw_1_creature,draw_1_creature,deal_2_spell,deal_2_spell,deal_2_spell",
            "draw_1_creature,draw_1_creature,draw_1_creature,draw_1_creature,deal_2_spell,deal_2_spell,deal_2_spell",
            "DefaultSettings")

        state_original = string_to_game_state(state_str)  # type: GameState
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