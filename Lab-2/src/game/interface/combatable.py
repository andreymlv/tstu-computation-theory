from typing import NamedTuple

from game.weapons.weapon import Weapon


class Combatable(NamedTuple):
    hp: int
    armor: int
    damage: int
    weapon: Weapon
    name: str = ""

    def is_dead(self) -> bool:
        return self.hp <= 0
