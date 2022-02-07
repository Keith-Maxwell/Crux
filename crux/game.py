from dataclasses import dataclass, field

from crux.decks import Deck
from crux.player import Player


class Game:
    def __init__(self) -> None:
        self.players: list[Player] = [].copy()

    @property
    def n_players(self):
        return len(self.players)

    def create_player(self, name) -> Player:
        player = Player(
            name=name,
            cards=[],
            problem_card=None,
            can_play=True,
            beta_spray=False,
        )
        self.players.append(player)
        return player

    def prepare_game(self):
        self.play_deck = Deck.create_play_deck()
        self.play_deck.shuffle()
        self.problem_deck = Deck.create_problem_deck()
        self.problem_deck.shuffle()
        for player in self.players:
            player.draw_problem(self.problem_deck)
            for _ in range(5):
                player.draw(self.play_deck)
