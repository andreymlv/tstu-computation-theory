from dataclasses import dataclass

from game.cursor import Cursor
from game.drawable import Drawable
from game.landscapes.landscape import Landscape
from game.position import Position
from game.units.blank import Blank
from game.units.unit import Unit


@dataclass()
class Cell(Drawable):
    position: Position
    unit: Unit | Blank
    cursor: Cursor | Blank
    landscape: Landscape

    def draw(self) -> str:
        return self.landscape.combine(self.unit)
