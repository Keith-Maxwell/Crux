
import logging

from crux.cards import ActionCard, HoldCard, ProblemCard
from crux.player import Player


def game_setup(player_names: list[str]):
    """Creates the game, with one playing deck and one problem deck and makes the players draw their initial hand cards

    Parameters
    ----------
    player_names : list[str]
        Names of the players

    Returns
    -------
    tuple[list[PlayerHand], PlayingDeck, ProblemDeck]
        A tuple containing the players, the playing deck and the problem deck
    """
    # Create the decks
    main_deck = PlayingDeck()
    problem_deck = ProblemDeck()
    main_deck.shuffle()
    problem_deck.shuffle()

    # Create the players
    players = []
    for i in range(len(player_names)):
        players.append(PlayerHand(player_names[i]))

    # make each player draw 5 cards + 1 problem card
    for player_hand in players:
        for _ in range(5):
            player_hand.draw(main_deck)
        player_hand.problem_card = problem_deck.cards.pop()

    return players, main_deck, problem_deck


def create_game(player_names: list[str]) -> tuple[list[PlayerHand], PlayingDeck, ProblemDeck]:
    """Create the elements of the game and makes sure the game can properly start

    Parameters
    ----------
    player_names : list[str]
        the players' names

    Returns
    -------
    tuple[list[PlayerHand], PlayingDeck, ProblemDeck]
        A tuple containing the players, the playing deck and the problem deck
    """
    game_setup_ok: bool = False
    while not game_setup_ok:
        # Create the game, with one playing deck and one problem deck
        # as well as the players
        players, main_deck, problem_deck = game_setup(player_names)

        # Ensure that no player has already won
        if any([check_win(player) is True for player in players]):
            game_setup_ok = False
        else:
            game_setup_ok = True
    return players, main_deck, problem_deck


def check_win(player: PlayerHand) -> bool:
    """Checks if the player has won the game with his current cards.
    To win, the player needs to have the cards necessary to complete his problem card.

    Parameters
    ----------
    player : PlayerHand
        The player to check

    Returns
    -------
    bool
        True if the player won, False otherwise
    """
    # Extract the 5 needed colors from the player's problem card
    colors_to_have = player.problem_card.name.split("_")
    # we make a copy of the list to avoid modifying the original
    player_cards = player.cards.copy()

    for color in colors_to_have:
        color_found = False
        for card in player_cards:
            if card.name == color:  # The player has the right color
                player_cards.remove(card)
                color_found = True
                break
            elif card.name == "FLASH":  # The player has the FLASH card
                player_cards.remove(card)
                color_found = True
                break
            else:  # The current card is not the right color
                continue  # check the next card
        if not color_found:  # current color not found, no need to check others
            return False
    # Every color was found
    return True


def validate_name(input_str: str) -> bool:
    """Check if the name is valid

    Parameters
    ----------
    input_str : str
        the input from the user

    Returns
    -------
    bool
        True if the name is valid, False otherwise
    """
    if input_str == "":
        return False
    return True


def validate_number(input_str: str, max_n: int, min_n: int) -> bool:
    """Check if the number is valid

    Parameters
    ----------
    input_str : str
        The input from the user
    max_n : int
        max value
    min_n : int
        min value

    Returns
    -------
    bool
        True if the number is valid, False otherwise
    """
    if input_str == "":
        return False
    try:
        return int(input_str) <= max_n and int(input_str) >= min_n
    except ValueError:
        return False


def ask_number_of_players() -> int:
    """Ask the user for the number of players

    Returns
    -------
    int
        validated number of players
    """    """"""
    while True:
        print("How many players? (2-5)")
        input_str = console.input()
        if validate_number(input_str, max_n=5, min_n=2):
            return int(input_str)
        else:
            print("Invalid input")


# ask all the names of the players
def ask_player_names(number_of_players: int) -> list[str]:
    """Ask the user for the names of the players

    Parameters
    ----------
    number_of_players : int
        number of players

    Returns
    -------
    list[str]
        validated names of the players
    """
    names: list[str] = []
    for n in range(number_of_players):
        while True:
            name = console.input(f"Enter the name of player {n + 1}: ")
            if validate_name(name):
                names.append(name)
                break
            else:
                console.print("Invalid input, try again")
    return names


def game_loop():

    # Ask the number of players
    n_players = ask_number_of_players()

    # Ask all the names of the players
    player_names = ask_player_names(n_players)

    # Setup the game
    players, main_deck, problem_deck = create_game(player_names)

    # game loop
    game_finished: bool = False
    while not game_finished:
        for player in players:

            console.rule(f"{player.player_name}'s turn")

            card_draw = player.draw(main_deck)
            console.print("you drew : ")
            card_draw.print()

            console.print("your current hand : ")
            player.print()

            console.print("your current problem card : ")
            player.problem_card.print()

            card_index_to_discard = console.input("Choose a card to discard (1-6): ")
            while validate_number(card_index_to_discard, max_n=6, min_n=1) is False:
                console.print("Invalid input, try again")
                card_index_to_discard = console.input("Choose a card to discard (1-6): ")

            card_index_to_discard = int(card_index_to_discard) - 1
            discarded_card = player.discard(card_index_to_discard, main_deck)

            # if the discarded card is an action card, execute the corresponding action
            match discarded_card.name:
                case "BETA_SPRAY":
                    beta_spray()
                case "BAIL":
                    bail()
                case "ROUTESETTER":
                    routesetter()
                case "THIEVING_DOG":
                    thieving_dog()
                case "DYNO":
                    dyno()
                case "GEAR_SWAP":
                    gear_swap()
                case "GUIDEBOOK":
                    guidebook()

            game_finished = check_win(player)
            if game_finished:
                console.print(f"{player.player_name} won the game!")
                break

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    game_loop()
