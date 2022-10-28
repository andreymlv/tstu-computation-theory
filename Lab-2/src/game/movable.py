from dataclasses import dataclass

from game.position import Position


@dataclass()
class Movable:
    position: Position
    speed: int
