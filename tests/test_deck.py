from crux.cards import ActionCard, HoldCard, ProblemCard
from crux.decks import Deck


def test_deck_card_count():
    main_deck = Deck.create_play_deck()
    problem_deck = Deck.create_problem_deck()
    assert main_deck.number_of_cards == 49
    assert problem_deck.number_of_cards == 6


def test_problem_deck_unique():
    problem_deck = Deck.create_problem_deck()
    problem_deck_list = [card.name for card in problem_deck.cards]
    assert len(problem_deck_list) == len(set(problem_deck_list))


def test_problem_deck_type():
    problem_deck = Deck.create_problem_deck()
    for card in problem_deck.cards:
        assert isinstance(card, ProblemCard)


def test_play_deck_type():
    main_deck = Deck.create_play_deck()
    for card in main_deck.cards:
        assert isinstance(card, HoldCard) or isinstance(card, ActionCard)


# def test_check_win_false():
#     hand = PlayerHand("Max")
#     hand.cards = [
#         Card(HoldCard.GREEN),
#         Card(HoldCard.GREEN),
#         Card(HoldCard.GREEN),
#         Card(HoldCard.GREEN),
#         Card(HoldCard.GREEN),
#     ]
#     hand.problem_card = Card(ProblemCard.GREEN_GREEN_BLUE_BLUE_PURPLE)
#     assert not check_win(hand)


# def test_check_win_true():
#     hand = PlayerHand("Max")
#     hand.cards = [
#         Card(HoldCard.GREEN),
#         Card(HoldCard.GREEN),
#         Card(HoldCard.BLUE),
#         Card(HoldCard.BLUE),
#         Card(HoldCard.PURPLE),
#     ]
#     hand.problem_card = Card(ProblemCard.GREEN_GREEN_BLUE_BLUE_PURPLE)
#     assert check_win(hand)


# def test_check_win_true_flash():
#     hand = PlayerHand("Max")
#     hand.cards = [
#         Card(HoldCard.GREEN),
#         Card(HoldCard.GREEN),
#         Card(ActionCard.FLASH),
#         Card(HoldCard.BLUE),
#         Card(HoldCard.PURPLE),
#     ]
#     hand.problem_card = Card(ProblemCard.GREEN_GREEN_BLUE_BLUE_PURPLE)
#     assert check_win(hand)


# def test_check_win_true_shuffle():
#     hand = PlayerHand("Max")
#     hand.cards = [
#         Card(HoldCard.GREEN),
#         Card(HoldCard.GREEN),
#         Card(HoldCard.BLUE),
#         Card(HoldCard.BLUE),
#         Card(HoldCard.PURPLE),
#     ]
#     hand.problem_card = Card(ProblemCard.GREEN_GREEN_BLUE_BLUE_PURPLE)
#     hand.shuffle()
#     assert check_win(hand)


# def test_validate_number():
#     assert validate_number("1", max_n=5, min_n=0) is True
#     assert validate_number("9", max_n=5, min_n=0) is False
#     assert validate_number("6", max_n=6, min_n=0) is True
#     assert validate_number("", max_n=6, min_n=0) is False
#     assert validate_number("hello", max_n=6, min_n=0) is False
#     assert validate_number("0", max_n=6, min_n=4) is False
#     assert validate_number("0", max_n=0, min_n=0) is True
