import json

from core_game.events.event import Event
from core_game.state.game_state import GameState


class Action:
    def __init__(self, action_str: str):
        """
        action_str should be a json object
        representing a dictionary. The dictionary will contain
        type, player, and a details sub-dictionary.
        """
        action_object = json.loads(action_str)
        self.type = action_object['type']  # type: str
        self.player_originating = action_object['player']  # type: int
        self.details = action_object['details']  # type: dict[str,ID]
        self.details['player_source'] = self.player_originating

        # self.event_types = {"play": self.play,
        #                "options": self.options,
        #                "attack": self.attack,
        #                "end": self.end,
        #                "target": self.target,
        #                "activate": self.activate}

    def get_event(self, state: GameState) -> Event:
        return Event(self.type, self.details)

        # def play(self,state : GameState) -> Event:
        #     """
        #     details should contain:
        #     card : single id, the id of the card to play
        #     """
        #     if state.contains_id(self.details['card']):
        #         return Event(self.type,self.details)
        #     return None
        #
        # def options(self,state : GameState) -> Event:
        #     pass
        #
        # def attack(self,state : GameState) -> Event:
        #     pass
        #
        # def end(self,state : GameState) -> Event:
        #     pass
        #
        # def target(self,state : GameState) -> Event:
        #     pass
        #
        # def activate(self,state : GameState) -> Event:
        #     pass
        #





        # play a card
        # choose something from a list of options
        # attack
        # end turn
        # choose a target
        # activate a card
