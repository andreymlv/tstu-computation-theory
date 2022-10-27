from position import Position
from unit import Unit
from weapons.melee_weapon import MeleeWeapon


class Melee(Unit):
    def __init__(self, position: Position, weapon: MeleeWeapon):
        super().__init__(position, 16, 16, 1, 4, weapon)

    def draw(self) -> str:
        return "M"
