from game.combatable import Combatable
from game.units.unit import Unit
from game.weapons.melee_weapon import MeleeWeapon


class Melee(Unit, Combatable):
    weapon: MeleeWeapon

    def draw(self) -> str:
        return "M"
