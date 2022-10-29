from typing import Self, NamedTuple

from game.display.cell import Cell
from game.display.position import Position
from game.display.screen import Screen


class Field(NamedTuple):
    screen: Screen
    cells: list[list[Cell]]

    def swap(self, position_from: Position, position_to: Position) -> Self:
        if self.is_inside(position_from) and self.is_inside(position_to):
            (
                self.cells[position_from.x][position_from.y],
                self.cells[position_to.x][position_to.y],
            ) = (
                self.cells[position_to.x][position_to.y],
                self.cells[position_from.x][position_from.y],
            )
            return self
        return self

    def is_inside(self, position: Position) -> bool:
        return self.screen.width > position.x >= 0 and self.screen.height > position.y >= 0

    def render(self) -> list[list[str]]:
        result: list[list[str]] = [[""] * self.screen.width] * self.screen.height
        for y in range(self.screen.height):
            for x in range(self.screen.width):
                result[y][x] = self.cells[y][x].draw()
        return result
