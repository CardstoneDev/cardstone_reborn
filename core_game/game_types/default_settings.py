from core_game.state.settings import SETTINGS

class DefaultSettings(SETTINGS):
    def get_initial_hand_size(self):
        return 4