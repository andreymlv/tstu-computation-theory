from dataclasses import dataclass

from position import Position


@dataclass()
class Movable:
    position: Position
    speed: int
