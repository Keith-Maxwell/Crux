from dataclasses import dataclass

from crux.actions import CardEffect


@dataclass
class Controller:
    def execute(self, action: CardEffect) -> None:
        action.execute()
