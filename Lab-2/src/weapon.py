from dataclasses import dataclass


@dataclass()
class Weapon:
    durability: int
    damage: int
    distance: int
