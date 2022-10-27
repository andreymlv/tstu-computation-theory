from dataclasses import dataclass

from weapon import Weapon


@dataclass()
class Combatable:
    hp: int
    armor: int
    damage: int
    weapon: Weapon

    def is_dead(self) -> bool:
        return self.hp <= 0
