from dataclasses import dataclass
from typing import Self

from game.cell import Cell
from game.position import Position


@dataclass()
class Field:
    width: int
    height: int
    cells: list[list[Cell]]

    def move(self, position_from: Position, position_to: Position) -> Self:
        if self.inside_field(position_from) and self.inside_field(position_to):
            cells = self.cells
            cell_from = self.cells[position_from.x][position_from.y]
            cell_to = self.cells[position_to.x][position_to.y]
            cells[position_from.x][position_from.y] = cell_to
            cells[position_to.x][position_to.y] = cell_from
            return Field(self.width, self.height, cells)

    def inside_field(self, position: Position) -> bool:
        return self.width > position.x >= 0 and self.height > position.y >= 0

    def render(self) -> list[list[str]]:
        result: list[list[str]] = [[""] * self.width] * self.height
        for x in range(self.height):
            for y in range(self.width):
                result[x][y] = self.cells[x][y].draw()
        return result
