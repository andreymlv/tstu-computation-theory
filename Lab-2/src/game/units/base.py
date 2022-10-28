from dataclasses import dataclass
from typing import Self

from game.units.unit import Unit


@dataclass()
class Base(Unit):
    can_produce: bool
    maximum_count_warriors: int
    warriors: list[Unit]

    def draw(self) -> str:
        return super().draw() + "B"

    def produce(self, warrior: Unit) -> Self:
        if self.can_produce:
            can_produce: bool = len(self.warriors) + 1 < self.maximum_count_warriors
            return Base(
                can_produce, self.maximum_count_warriors, self.warriors + [warrior]
            )
        return self
