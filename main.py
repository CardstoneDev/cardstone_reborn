import sys
import core_game

DO_TEST = True

if __name__ == "__main__":
    if DO_TEST or sys.argv[1] == "test":
        from core_game.test.coregame_test import static_game_functionality
        static_game_functionality.do_test()
        from core_game.test.coregame_test import basic_action_functionality
        basic_action_functionality.do_test()