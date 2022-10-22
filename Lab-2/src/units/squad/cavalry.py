from position import Position
from units.unit import Unit
from weapon.weapon import Weapon


class Cavalry(Unit):
    def __init__(self, position: Position, weapon: Weapon):
        super().__init__(position, 16, 16, 1, 4, weapon)

    def draw(self) -> str:
        return "C"
