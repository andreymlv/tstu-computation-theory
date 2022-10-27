from game.weapons.weapon import Weapon


class RangeWeapon(Weapon):
    def __init__(self, durability: int, damage: int):
        super().__init__(durability, damage, 8)
