from game.combatable import Combatable
from game.units.unit import Unit
from game.weapons.range_weapon import RangeWeapon


class Range(Unit, Combatable):
    weapon: RangeWeapon

    def draw(self) -> str:
        return "R"
