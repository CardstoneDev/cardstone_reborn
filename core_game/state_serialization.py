import json
import pickle
from core_game.state.action import Action
from core_game.state.card_list import CardList
from core_game.state.game_state import GameState
from core_game.state.mana_pool import ManaPool
from core_game.state.player import Player
from core_game.state.player_cards import PlayerCards
from core_game.state.settings import SETTINGS
from core_game.devotions.no_devotion import NoDevotion
from core_game.game_types import *
from core_game.cards.game_cards import *

def string_to_action(input: str) -> Action:
    return Action(input)


def string_to_game_state(input: str) -> GameState:
    return pickle.loads(input)


def game_state_to_string(state: GameState) -> str:
    return pickle.dumps(state)

def parse_settings(settings_str: str) -> SETTINGS:
    return eval(settings_str + "()")

def parse_deck_list(deck_list_str: str,player : Player) -> CardList:
    return CardList([eval(x+"(player)") for x in json.loads(deck_list_str)])


def deck_lists_to_game_state(deck_list0_str:str,deck_list1_str:str,settings_str:str) -> GameState:
    settings = parse_settings(settings_str)
    init_mana = settings.get_initial_mana()
    p0 = Player(None,NoDevotion(),ManaPool(init_mana,init_mana),settings.get_initial_health())
    p1 = Player(None,NoDevotion(),ManaPool(init_mana,init_mana),settings.get_initial_health())
    player_cards0 = PlayerCards(parse_deck_list(deck_list0_str, p0),CardList([]),CardList([]),CardList([]),CardList([]))
    player_cards1 = PlayerCards(parse_deck_list(deck_list1_str, p1), CardList([]), CardList([]), CardList([]), CardList([]))
    p0.cards = player_cards0
    p1.cards = player_cards1
    return GameState(p0,p1,settings.get_starting_player(),settings)
