from game.interface.combatable import Combatable
from game.interface.drawable import Drawable
from game.weapons.range_weapon import RangeWeapon


class Range(Drawable, Combatable):
    weapon: RangeWeapon

    def draw(self) -> str:
        return "R"
