from typing import NamedTuple

from game.display.position import Position


class Movable(NamedTuple):
    position: Position
    speed: int
