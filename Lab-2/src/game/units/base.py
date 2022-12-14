from dataclasses import dataclass
from typing import Self

from game.interface.combatable import Combatable
from game.interface.drawable import Drawable


@dataclass()
class Base(Drawable):
    can_produce: bool
    maximum_count_warriors: int
    warriors: list[Combatable]

    def draw(self) -> str:
        return " " if self.is_crushed() else "B"

    def produce(self, warrior: Combatable) -> Self:
        if self.can_produce:
            can_produce: bool = len(self.warriors) + 1 < self.maximum_count_warriors
            return Base(
                can_produce, self.maximum_count_warriors, self.warriors + [warrior]
            )
        return self

    def is_crushed(self) -> bool:
        return len(self.warriors) == 0 or all(
            map(lambda warrior: warrior.is_dead(), self.warriors)
        )
