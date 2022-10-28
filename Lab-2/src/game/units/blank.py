from dataclasses import dataclass

from game.units.unit import Unit


@dataclass()
class Blank(Unit):
    def draw(self) -> str:
        return " "
