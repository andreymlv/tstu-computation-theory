from typing import Self, NamedTuple

from multipledispatch import dispatch

from game.display.cell import Cell
from game.display.position import Position
from game.display.screen import Screen
from interface.drawable import Drawable
from units.cursor import Cursor


class Field(NamedTuple):
    screen: Screen
    cells: list[list[Cell]]

    @dispatch(Cursor, Position, Position)
    def move_cell(
        self, item: Cursor, position_from: Position, position_to: Position
    ) -> Self:
        raise NotImplementedError()

    @dispatch(Drawable, Position, Position)
    def move_cell(
        self, item: Drawable, position_from: Position, position_to: Position
    ) -> Self:
        raise NotImplementedError()

    def swap_cell(self, position_from: Position, position_to: Position) -> Self:
        if self.is_inside(position_from) and self.is_inside(position_to):
            (
                self.cells[position_from.y][position_from.x],
                self.cells[position_to.y][position_to.x],
            ) = (
                self.cells[position_to.y][position_to.x],
                self.cells[position_from.y][position_from.x],
            )
            return self
        return self

    def is_inside(self, position: Position) -> bool:
        return (
            self.screen.width > position.x >= 0 and self.screen.height > position.y >= 0
        )

    def render(self) -> list[list[str]]:
        result: list[list[str]] = []
        for y in range(self.screen.height):
            for x in range(self.screen.width):
                if y == 0:
                    result.append([])
                result[y].append(self.cells[y][x].draw())
        return result
