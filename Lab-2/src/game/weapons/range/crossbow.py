from game.weapons.range_weapon import RangeWeapon


class Crossbow(RangeWeapon):
    def __init__(self):
        super().__init__(256, 8)