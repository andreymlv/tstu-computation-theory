from game.interface.drawable import Drawable
from game.interface.combatable import Combatable
from game.weapons.melee_weapon import MeleeWeapon


class Melee(Drawable, Combatable):
    weapon: MeleeWeapon

    def draw(self) -> str:
        return "M"
