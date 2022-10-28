from game.weapons.melee_weapon import MeleeWeapon


class Dagger(MeleeWeapon):
    def __init__(self):
        super().__init__(128, 4)
