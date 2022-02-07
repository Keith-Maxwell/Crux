import logging
from dataclasses import dataclass
from random import randint
from typing import Protocol

from crux.decks import Deck
from crux.player import Player


class CardEffect(Protocol):
    def execute(self) -> None:
        ...


@dataclass
class Draw:
    """a player draws a card from the deck"""

    player: Player
    deck: Deck

    def execute(self) -> None:
        card = self.deck.cards.pop()
        self.player.cards.append(card)
        logging.info(f"{self.player.name} draws {card}")


@dataclass
class Dyno:
    """Skips the next player's turn"""

    next_player: Player

    def execute(self) -> None:
        self.next_player.can_play = False
        logging.info(f"{self.next_player.name} is skipped")


@dataclass
class Bail:
    """The player of your choice discards all his cards ands draws a new hand"""

    target_player: Player
    play_deck: Deck

    def execute(self) -> None:
        for _ in range(5):
            discarded_card = self.target_player.cards.pop()
            self.play_deck.cards.insert(0, discarded_card)
        logging.info(f"{self.target_player.name} discards their hand")
        for _ in range(5):
            self.target_player.draw(self.play_deck)
        logging.info(f"{self.target_player.name} draws a new hand")


@dataclass
class Flash:
    """Wild card, can be used as any hold card."""

    def execute(self) -> None:
        logging.info("Why would you do this ???")


@dataclass
class Thieving_dog:
    """Choose a player, give him a card from your hand, and draw a card from his hand"""

    target_player: Player
    origin_player: Player
    index_of_card_to_give: int

    def execute(self) -> None:
        logging.info(
            f"{self.origin_player.name} gives {self.target_player.name} a card"
        )
        card_to_give = self.origin_player.cards.pop(self.index_of_card_to_give)
        self.target_player.cards.append(card_to_give)
        logging.info(
            f"{self.origin_player.name} draws a card from {self.target_player.name}"
        )
        card_to_steal = self.target_player.cards.pop(randint(0, 5))
        self.origin_player.cards.append(card_to_steal)


@dataclass
class Beta_spray:
    """The player of your choice makes his hand visible to all until your next turn"""

    target_player: Player

    def execute(self) -> None:
        self.target_player.beta_spray = True
        logging.info(f"{self.target_player.name}'s hand is now visible")


@dataclass
class Gear_swap:
    """Every player gives a card to the player on his left"""

    list_of_players: list[Player]

    def execute(self) -> None:
        for i in range(len(self.list_of_players)):
            current_player = self.list_of_players[i]
            # Left player is the next one modulo the number of players, so it loops back to the first player
            left_player = self.list_of_players[
                (i + 1) % len(self.list_of_players)
            ]
            card_to_give = current_player.cards.pop(current_player.ask_card())
            left_player.cards.append(card_to_give)


@dataclass
class Guidebook:
    """You can look at the hand of the player of your choice"""

    pass


@dataclass
class Routesetter:
    """You can switch your problem card with the one of the player of your choice"""

    target_player: Player
    origin_player: Player

    def execute(self) -> None:
        self.target_player.problem_card, self.origin_player.problem_card = (
            self.origin_player.problem_card,
            self.target_player.problem_card,
        )
