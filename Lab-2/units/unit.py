from object import Object
from position import Position
from weapon.weapon import Weapon


class Unit(Object):
    def __init__(self, position: Position, hp: int, armor: int, speed: int, damage: int, weapon: Weapon):
        super().__init__(position)
        self.hp = hp
        self.armor = armor
        self.speed = speed
        self.damage = damage
        self.weapon = weapon

    def draw(self) -> str:
        return super().draw() + "U"

    def is_dead(self) -> bool:
        return self.hp <= 0
