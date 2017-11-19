import abc
class SETTINGS:
    @abc.abstractmethod
    def get_initial_hand_size(self):
        pass

    @abc.abstractmethod
    def get_initial_health(self):
        pass
