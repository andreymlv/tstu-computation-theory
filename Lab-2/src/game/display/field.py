from typing import Self, NamedTuple

from game.display.cell import Cell
from game.display.position import Position
from game.display.screen import Screen
from game.units.blank import Blank
from game.units.cursor import Cursor


class Field(NamedTuple):
    screen: Screen
    cells: list[list[Cell]]

    def move_cursor(self, position_from: Position, position_to: Position) -> Self:
        if self.is_possible_move(position_from, position_to):
            if self.cells[position_from.x][position_from.y].cursor is Cursor():
                self.cells[position_from.x][position_from.y].cursor = Blank()
                self.cells[position_to.x][position_to.y].cursor = Cursor()
        return self

    def move_unit(self, position_from: Position, position_to: Position) -> Self:
        if self.is_possible_move(position_from, position_to):
            pass
        return self

    def swap_cell(self, position_from: Position, position_to: Position) -> Self:
        if self.is_possible_move(position_from, position_to):
            (
                self.cells[position_from.x][position_from.y],
                self.cells[position_to.x][position_to.y],
            ) = (
                self.cells[position_to.x][position_to.y],
                self.cells[position_from.x][position_from.y],
            )
        return self

    def is_inside(self, position: Position) -> bool:
        return (
            self.screen.width > position.x >= 0 and self.screen.height > position.y >= 0
        )

    def is_possible_move(self, position_from: Position, position_to: Position) -> bool:
        return self.is_inside(position_from) and self.is_inside(position_to)

    def render(self) -> list[list[str]]:
        result: list[list[str]] = []
        for x in range(self.screen.width):
            for y in range(self.screen.height):
                if y == 0:
                    result.append([])
                result[x].append(self.cells[x][y].draw())
        return result
