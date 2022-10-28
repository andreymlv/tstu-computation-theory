from dataclasses import dataclass
from typing import Self

from game.cell import Cell
from game.position import Position


@dataclass()
class Field:
    width: int
    height: int
    cells: list[list[Cell]]

    def swap(self, position_from: Position, position_to: Position) -> Self:
        if self.inside_field(position_from) and self.inside_field(position_to):
            (
                self.cells[position_from.x][position_from.y],
                self.cells[position_to.x][position_to.y],
            ) = (
                self.cells[position_to.x][position_to.y],
                self.cells[position_from.x][position_from.y],
            )
            return Field(self.width, self.height, self.cells)
        return self

    def inside_field(self, position: Position) -> bool:
        return self.width > position.x >= 0 and self.height > position.y >= 0

    def render(self) -> list[list[str]]:
        result: list[list[str]] = [[""] * self.width] * self.height
        for x in range(self.height):
            for y in range(self.width):
                result[x][y] = self.cells[x][y].draw()
        return result
