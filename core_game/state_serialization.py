from core_game.state.action import Action
from core_game.state.card_list import CardList
from core_game.state.game_state import GameState
from core_game.state.mana_pool import ManaPool
from core_game.state.player import Player
from core_game.state.player_cards import PlayerCards


def string_to_action(input: str) -> Action:
    pass


def string_to_game_state(input: str) -> GameState:
    pass


def game_state_to_string(state: GameState) -> str:
    pass


def deck_lists_to_game_state(deck_list0_str:str,deck_list1_str:str,settings_str:str) -> GameState:
    settings = get_settings_instance(settings_str)
    init_mana = settings.get_initial_mana()
    player_cards0 = PlayerCards(create_deck_list(deck_list0_str),CardList([]),CardList([]),CardList([]),CardList([]))
    player_cards1 = PlayerCards(create_deck_list(deck_list1_str), CardList([]), CardList([]), CardList([]), CardList([]))
    p0 = Player(player_cards0,NoDevotion(),ManaPool(init_mana,init_mana),settings.get_initial_health())
    p1 = Player(player_cards1,NoDevotion(),ManaPool(init_mana,init_mana),settings.get_initial_health())
    return GameState(p0,p1,settings.get_starting_player(),settings)