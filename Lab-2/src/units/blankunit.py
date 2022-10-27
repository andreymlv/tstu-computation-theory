from dataclasses import dataclass

from unit import Unit


@dataclass()
class BlankUnit(Unit):
    def draw(self) -> str:
        return ""
