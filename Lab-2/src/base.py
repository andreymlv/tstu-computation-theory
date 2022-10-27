from dataclasses import dataclass

from combatable import Combatable
from unit import Unit
from weapons.weaponless import Weaponless


@dataclass()
class Base(Unit, Combatable):
    can_produce: bool
    maximum_count_warriors: int
    warriors: list[Unit]

    def draw(self) -> str:
        return super().draw() + "^"

    def produce(self, warrior: Unit):
        if self.can_produce:
            can_produce: bool = len(self.warriors) + 1 < self.maximum_count_warriors
            return Base(
                128,
                8,
                0,
                Weaponless(),
                self.position,
                0,
                can_produce,
                self.maximum_count_warriors,
                self.warriors + [warrior],
            )
        return self
