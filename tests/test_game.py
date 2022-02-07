from crux.game import Game


def test_create_1_player():
    game = Game()
    player1 = game.create_player("player1")
    assert len(game.players) == 1
    assert player1.name == "player1"
    assert len(player1.cards) == 0
    assert player1.problem_card is None
    assert player1.can_play is True
    assert player1.beta_spray is False


def test_create_2_players():
    game = Game()
    player1 = game.create_player("player1")
    player2 = game.create_player("player2")
    assert len(game.players) == 2
    assert player1.name == "player1"
    assert player2.name == "player2"
    assert len(player1.cards) == 0
    assert len(player2.cards) == 0
    assert player1.problem_card is None
    assert player2.problem_card is None
    assert player1.can_play is True
    assert player2.can_play is True
    assert player1.beta_spray is False
    assert player2.beta_spray is False


def test_prepare_game_decks():
    game = Game()
    game.prepare_game()
    assert len(game.play_deck.cards) == 49
    assert len(game.problem_deck.cards) == 6


def test_prepare_game_1player():
    game = Game()
    player1 = game.create_player("player1")
    game.prepare_game()
    assert len(player1.cards) == 5
    assert len(game.play_deck.cards) == 49 - 5
    assert len(game.problem_deck.cards) == 6 - 1


def test_prepare_game_2players():
    game = Game()
    player1 = game.create_player("player1")
    player2 = game.create_player("player2")
    game.prepare_game()
    assert len(player1.cards) == 5
    assert len(player2.cards) == 5
    assert len(game.play_deck.cards) == 49 - 5 * 2
    assert len(game.problem_deck.cards) == 6 - 1 * 2
    assert player1.problem_card is not None
    assert player1.problem_card != player2.problem_card
