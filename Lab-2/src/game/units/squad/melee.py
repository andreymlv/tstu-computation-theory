from game.position import Position
from game.units.unit import Unit
from game.weapons.melee_weapon import MeleeWeapon


class Melee(Unit):
    def __init__(self, position: Position, weapon: MeleeWeapon):
        super().__init__(position, 16, 16, 1, 4, weapon)

    def draw(self) -> str:
        return "M"