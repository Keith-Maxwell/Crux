from dataclasses import dataclass
from enum import Enum


@dataclass
class HoldCard:
    color: str
    type: str
    description: str


@dataclass
class ProblemCard:
    name: str
    holds_needed: list[HoldCard]


@dataclass
class ActionCard:
    name: str
    description: str


class ActionsEnum(Enum):
    FLASH = {
        "name": "flash",
        "description": "Wild card, can be used as any hold card.",
    }
    ROUTESETTER = {
        "name": "routesetter",
        "description": "Swap your problem card with another player",
    }
    THIEVING_DOG = {
        "name": "thieving_dog",
        "description": "Give another player one of your cards, then take one of theirs",
    }
    BETA_SPRAY = {
        "name": "beta_spray",
        "description": "Choose a player. They must display ALL of  their cards until your next turn",
    }
    BAIL = {
        "name": "bail",
        "description": "Choose a player. They must discard all of their play cards and pick up 5 new cards",
    }
    DYNO = {"name": "dyno", "description": "skip the next player's turn"}
    GEAR_SWAP = {
        "name": "gear_swap",
        "description": "Everyone must pass one card to the left",
    }
    GUIDEBOOK = {
        "name": "guidebook",
        "description": "Choose one player and look at ALL of their cards",
    }


class HoldsEnum(Enum):
    GREEN = {
        "color": "green",
        "type": "crimp",
        "description": "A tiny hold usually only big enough for a single pad.",
    }
    BLUE = {
        "color": "blue",
        "type": "sloper",
        "description": "A tricky sloping hold with no lip or edge of any kind. They rely on maximum surface area for friction.",
    }
    PURPLE = {
        "color": "purple",
        "type": "pocket",
        "description": "A indented hold that is usually big enough for between 1 and 3 fingers.",
    }
    PINK = {
        "color": "pink",
        "type": "jug",
        "description": "Large and easy to grab holds. Perfect for beginners or when you need a rest.",
    }


class ProblemsEnum(Enum):
    GREEN_PURPLE_PURPLE_PINK_PINK = [
        HoldCard(**HoldsEnum.GREEN.value),
        HoldCard(**HoldsEnum.PURPLE.value),
        HoldCard(**HoldsEnum.PURPLE.value),
        HoldCard(**HoldsEnum.PINK.value),
        HoldCard(**HoldsEnum.PINK.value),
    ]
    BLUE_BLUE_PINK_PURPLE_PURPLE = [
        HoldCard(**HoldsEnum.BLUE.value),
        HoldCard(**HoldsEnum.BLUE.value),
        HoldCard(**HoldsEnum.PINK.value),
        HoldCard(**HoldsEnum.PURPLE.value),
        HoldCard(**HoldsEnum.PURPLE.value),
    ]
    GREEN_GREEN_PINK_PURPLE_PURPLE = [
        HoldCard(**HoldsEnum.GREEN.value),
        HoldCard(**HoldsEnum.GREEN.value),
        HoldCard(**HoldsEnum.PINK.value),
        HoldCard(**HoldsEnum.PURPLE.value),
        HoldCard(**HoldsEnum.PURPLE.value),
    ]
    BLUE_BLUE_PINK_PINK_PURPLE = [
        HoldCard(**HoldsEnum.BLUE.value),
        HoldCard(**HoldsEnum.BLUE.value),
        HoldCard(**HoldsEnum.PINK.value),
        HoldCard(**HoldsEnum.PINK.value),
        HoldCard(**HoldsEnum.PURPLE.value),
    ]
    GREEN_GREEN_PINK_PINK_PURPLE = [
        HoldCard(**HoldsEnum.GREEN.value),
        HoldCard(**HoldsEnum.GREEN.value),
        HoldCard(**HoldsEnum.PINK.value),
        HoldCard(**HoldsEnum.PINK.value),
        HoldCard(**HoldsEnum.PURPLE.value),
    ]
    GREEN_GREEN_BLUE_BLUE_PURPLE = [
        HoldCard(**HoldsEnum.GREEN.value),
        HoldCard(**HoldsEnum.GREEN.value),
        HoldCard(**HoldsEnum.BLUE.value),
        HoldCard(**HoldsEnum.BLUE.value),
        HoldCard(**HoldsEnum.PURPLE.value),
    ]
