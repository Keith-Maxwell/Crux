from __future__ import annotations

import random
from dataclasses import dataclass

from crux.cards import (
    ActionCard,
    ActionsEnum,
    HoldCard,
    HoldsEnum,
    ProblemCard,
    ProblemsEnum,
)


@dataclass
class Deck:
    cards: list

    @property
    def number_of_cards(self) -> int:
        return len(self.cards)

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    @staticmethod
    def create_problem_deck() -> Deck:
        cards: list[ProblemCard] = []
        for problem in ProblemsEnum:
            cards.append(ProblemCard(problem.name, problem.value))
        return Deck(cards)

    @staticmethod
    def create_play_deck() -> Deck:
        cards: list[HoldCard | ActionCard] = []
        for _ in range(6):
            for hold in HoldsEnum:
                cards.append(HoldCard(**hold.value))
        for _ in range(4):
            cards.append(ActionCard(**ActionsEnum.GEAR_SWAP.value))
            cards.append(ActionCard(**ActionsEnum.THIEVING_DOG.value))
            cards.append(ActionCard(**ActionsEnum.DYNO.value))
            cards.append(ActionCard(**ActionsEnum.ROUTESETTER.value))
        for _ in range(3):
            cards.append(ActionCard(**ActionsEnum.GUIDEBOOK.value))
        for _ in range(2):
            cards.append(ActionCard(**ActionsEnum.FLASH.value))
            cards.append(ActionCard(**ActionsEnum.BETA_SPRAY.value))
            cards.append(ActionCard(**ActionsEnum.BAIL.value))
        return Deck(cards)
