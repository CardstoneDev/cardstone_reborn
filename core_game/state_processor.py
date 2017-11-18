from core_game.state_serialization import string_to_action, string_to_game_state, game_state_to_string


def confirm(action_str: str, state_str: str) -> bool:
    """
    Takes an action and an input state, and returns
    a boolean whether that action is valid in the given input state
    """
    action = string_to_action(action_str)
    state = string_to_game_state(state_str)
    return state.can_do(action)


def process(action_str: str, state_str: str) -> str:
    """
    Takes an action and an input state, and returns
    a stringified version of the result of
    taking that action in that state.
    When exceptional events occur (game end, error, etc),
    calling analyze with the output will describe the event
    """
    action = string_to_action(action_str)
    state = string_to_game_state(state_str)
    state.do(action)
    return game_state_to_string(state)


def analyze(state_str: str) -> str:
    """
    Takes in the result of a call to process.
    If that result was a valid game state, returns "ok".
    If that result was an error, return "error: " followed by a descriptive error message.
    If that result ended the game, returns "end: " follwed by either 0 or 1, where 0
    indicates player 0 won and 1 indicates player 1 won.
    """
    pass


def render_string(state_str: str, player_num: int) -> str:
    """
    Takes a string representing a board state, and
    a number representing a player number: 0 or 1.
    Returns a string which can be sent to the frontend
    to render the board state for that player.
    """
