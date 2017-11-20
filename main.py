import sys
import core_game

if __name__ == "__main__":
    if sys.argv[1] == "test":
        from core_game.test.coregame_test import static_game_functionality
        static_game_functionality.do_test()
        from core_game.test.coregame_test import basic_action_functionality
        basic_action_functionality.do_test()