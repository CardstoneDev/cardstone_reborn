import abc


class SETTINGS(abc.ABC):
    @abc.abstractmethod
    def get_initial_hand_size(self) -> int:
        pass

    @abc.abstractmethod
    def get_initial_health(self) -> int:
        pass

    @abc.abstractmethod
    def get_initial_mana(self) -> int:
        pass

    @abc.abstractmethod
    def get_starting_player(self) -> int:
        pass
