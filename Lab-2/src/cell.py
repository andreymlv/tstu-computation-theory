from dataclasses import dataclass

from cursor import Cursor
from drawable import Drawable
from landscape import Landscape
from position import Position
from unit import Unit
from units.blankunit import BlankUnit


@dataclass()
class Cell(Drawable):
    position: Position
    unit: Unit | BlankUnit
    cursor: Cursor | BlankUnit
    landscape: Landscape

    def draw(self) -> str:
        return self.landscape.combine(self.unit)
