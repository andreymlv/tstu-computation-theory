from game.position import Position
from game.units.unit import Unit
from game.weapons.range_weapon import RangeWeapon


class Range(Unit):
    def __init__(self, position: Position, weapon: RangeWeapon):
        super().__init__(position, 8, 10, 1, 1, weapon)

    def draw(self) -> str:
        return "R"