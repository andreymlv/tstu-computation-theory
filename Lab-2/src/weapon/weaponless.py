from weapon.weapon import Weapon


class Weaponless(Weapon):
    def __init__(self):
        super().__init__(0, 0, 0)
