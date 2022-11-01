from dataclasses import dataclass

from game.display.position import Position
from game.interface.drawable import Drawable
from game.landscapes.landscape import Landscape
from game.units.blank import Blank
from game.units.cursor import Cursor


@dataclass()
class Cell(Drawable):
    position: Position
    unit: Drawable
    cursor: Cursor | Blank
    landscape: Landscape

    def draw(self) -> str:
        return self.landscape.combine(
            self.unit if self.cursor.draw() == " " else self.cursor
        )
