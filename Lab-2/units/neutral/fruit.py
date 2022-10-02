from position import Position
from units.unit import Unit
from weapon.weaponless import Weaponless


class Fruit(Unit):
    def __init__(self, position: Position):
        super().__init__(position, 0, 0, 0, 0, Weaponless())

    def draw(self) -> str:
        return "f"
