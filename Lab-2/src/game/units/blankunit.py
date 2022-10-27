from dataclasses import dataclass

from game.units.unit import Unit


@dataclass()
class BlankUnit(Unit):
    def draw(self) -> str:
        return ""
