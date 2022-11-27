from typing import NamedTuple

from src.size import Size


class Position(NamedTuple):
    x: float
    y: float

    def add(self, other):
        return Size(self.x + other.x, self.y + other.y)
