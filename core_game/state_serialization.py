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
# TODO: Generalize this
from core_game.game_types.default_settings import DefaultSettings
from core_game.cards.game_cards.creatures.neutral.draw_creature import DrawCreature

def string_to_action(input: str) -> Action:
    return Action(input)


def string_to_game_state(input: str) -> GameState:
    return pickle.loads(input)


def game_state_to_string(state: GameState) -> str:
    return pickle.dumps(state)

def parse_settings(settings_str: str) -> SETTINGS:
    return eval(settings_str + "()")

def parse_deck_list(deck_list_str: str,player : Player,cur_id : int) -> CardList:
    #TODO potentially worry about security
    global p
    p = player
    r = []
    for elt in json.loads(deck_list_str):
        card = eval(elt+"(p,"+str(cur_id)+")")
        cur_id += 1
        r.append(card)
    return CardList(r)


def deck_lists_to_game_state(deck_list0_str:str,deck_list1_str:str,settings_str:str) -> GameState:
    cur_id = 0
    settings = parse_settings(settings_str)
    init_mana = settings.get_initial_mana()
    p0 = Player(None,NoDevotion(),ManaPool(init_mana,init_mana),settings.get_initial_health())
    p1 = Player(None,NoDevotion(),ManaPool(init_mana,init_mana),settings.get_initial_health())
    player_cards0 = PlayerCards(parse_deck_list(deck_list0_str, p0,cur_id),CardList([]),CardList([]),CardList([]),CardList([]))
    cur_id += len(player_cards0.deck.cards)
    player_cards1 = PlayerCards(parse_deck_list(deck_list1_str, p1,cur_id), CardList([]), CardList([]), CardList([]), CardList([]))
    p0.cards = player_cards0
    p1.cards = player_cards1
    state = GameState(p0,p1,settings.get_starting_player(),settings,cur_id)
    state.get_active_player().mana.empty_crystals += 1
    state.get_active_player().mana.full_crystals += 1
    state.draw_starting_cards()
    return state
