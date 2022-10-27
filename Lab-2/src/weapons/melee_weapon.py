from weapon import Weapon


class MeleeWeapon(Weapon):
    def __init__(self, durability: int, damage: int):
        super().__init__(durability, damage, 1)
