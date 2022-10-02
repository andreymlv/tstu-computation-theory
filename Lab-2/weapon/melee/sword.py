from weapon.melee_weapon import MeleeWeapon


class Sword(MeleeWeapon):
    def __init__(self):
        super().__init__(512, 8)
