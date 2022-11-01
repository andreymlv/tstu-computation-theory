from turtle import color
from typing import Self, NamedTuple

import colorama

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

    def render(self) -> str:
        zipped_cells: zip[tuple[Cell]] = zip(*self.cells)
        transposed_cells: list[list[Cell]] = [list(row) for row in zipped_cells]
        result: str = ""
        for line in transposed_cells:
            for cell in line:
                result += cell.draw()
            result += colorama.Style.RESET_ALL + "\n"
        return result
