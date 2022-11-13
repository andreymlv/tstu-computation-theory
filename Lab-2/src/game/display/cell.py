from dataclasses import dataclass

from game.display.position import Position
from game.interface.drawable import Drawable
from game.landscapes.landscape import Landscape
from game.units.blank import Blank
from game.units.cursor import Cursor
from game.units.base import Base


@dataclass()
class Cell(Drawable):
    position: Position
    base: Base
    unit: Drawable
    cursor: Cursor | Blank
    landscape: Landscape

    def draw(self) -> str:
        to_draw: Drawable = Blank()
        if not self.base.is_crushed():
            to_draw = self.base
        elif self.unit.draw() != " ":
            to_draw = self.unit
        if self.cursor.draw() == " ":
            return self.landscape.combine(to_draw)
        return self.cursor.draw() + to_draw.draw()

    def can_enter(self) -> bool:
        return self.base.is_crushed() and self.unit == Blank()
