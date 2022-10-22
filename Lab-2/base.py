from position import Position
from units.unit import Unit
from weapon.weaponless import Weaponless


class Base(Unit):
    def __init__(
        self,
        position: Position,
        hp: int,
        can_produce: bool,
        maximum_count_warriors: int,
        warriors: list[Unit],
    ):
        super().__init__(position, hp, 0, 0, 0, Weaponless())
        self.maximum_count_warriors = maximum_count_warriors
        self.hp = hp
        self.can_produce = can_produce
        self.warriors = warriors

    def draw(self) -> str:
        return super().draw() + "^"

    def produce(self, warrior: Unit):
        if self.can_produce:
            can_produce: bool = len(self.warriors) + 1 < self.maximum_count_warriors
            return Base(
                self.position,
                self.hp,
                can_produce,
                self.maximum_count_warriors,
                self.warriors + [warrior],
            )
        return self

    def is_crushed(self):
        return self.hp <= 0 or len(self.warriors) == 0
