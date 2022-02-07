from dataclasses import dataclass

from crux.cards import HoldCard, ProblemCard


@dataclass
class Player:
    name: str
    cards: list[HoldCard]
    problem_card: ProblemCard
    can_play: bool
    beta_spray: bool

    def draw(self, deck) -> None:
        card = deck.cards.pop()
        self.cards.append(card)

    def draw_problem(self, deck) -> None:
        self.problem_card = deck.cards.pop()

    def ask_card(self) -> int:
        while True:
            try:
                index = int(
                    input(f"{self.name}, which card do you want to play? ")
                )
                if index > 0 and index < len(self.cards):
                    return index
            except ValueError:
                print("Invalid input, try again")
                continue
