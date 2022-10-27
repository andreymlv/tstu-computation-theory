from weapons.range_weapon import RangeWeapon


class Bow(RangeWeapon):
    def __init__(self):
        super().__init__(256, 6)
