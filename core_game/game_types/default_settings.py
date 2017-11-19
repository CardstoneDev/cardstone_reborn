from core_game.state.settings import SETTINGS


class DefaultSettings(SETTINGS):
    def get_starting_player(self) -> int:
        return 0

    def get_initial_mana(self) -> int:
        return 0

    def get_initial_health(self):
        return 3

    def get_initial_hand_size(self):
        return 4
